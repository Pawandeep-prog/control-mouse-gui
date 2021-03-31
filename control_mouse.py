import cv2
import numpy as np 
from detect_tip import detect_tip
import pyautogui
from tensorflow.keras.models import load_model
from select_tip import select_tip


def control_mouse(which_one):
	left, right = True, True

	model = load_model('handmodel_fingers_model.h5')

	print("="*50, "\nmodel loaded successfully")

	if which_one == "automatic":
		point, frame = detect_tip()

	else:
		point, frame = select_tip()
	print("+"*50, "Finger tip detcted successfully")


	print("="*50, "\nStarting Webcam")
	cap = cv2.VideoCapture(0)

	ix, iy = int(point[0]), int(point[1])

	old_pts = np.array([[ix, iy]], dtype=np.float32).reshape(-1,1,2)
	old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	mask = np.zeros_like(frame)

	color = (0,255,0)
	c=0
	while True:

	    _, new_frm = cap.read()
	    new_frm = cv2.flip(new_frm, 1)


	    new_gray = cv2.cvtColor(new_frm ,cv2.COLOR_BGR2GRAY)

	    new_pts,status,err = cv2.calcOpticalFlowPyrLK(old_gray, 
	                         new_gray, 
	                         old_pts, 
	                         None, maxLevel=1,
	                         criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
	                                                         15, 0.08))

	    key = cv2.waitKey(1)

	    if key == ord('e'):
	        mask = np.zeros_like(new_frm)

	    elif key == ord('c'):
	        color = (0,0,0)
	        lst = list(color)
	        c+=1
	        lst[c%3] = 255
	        color = tuple(lst)

	    elif key == ord('g'):
	        pass

	    elif key == ord('r'):
	    	cap.release()
	    	control_mouse(which_one)
	    	return

	    else:
	        for i, j in zip(old_pts, new_pts):
	            x,y = j.ravel()
	            a, b = i.ravel()

	            cv2.line(mask, (a,b), (x, y), color, 15)

	    cv2.circle(new_frm, (x,y), 3, (255,255,0), 2)

	    pyautogui.moveTo(int(x)*3,int(y*2.25))

	    ref = new_frm[int(y-10):int(y+160), int(x-40):int(x+100)]
	    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)

	    _, ref = cv2.threshold(ref, 120, 255, cv2.THRESH_BINARY_INV)
	    
	    ref = cv2.resize(ref, (128,128))

	    inp = np.reshape(ref, (1,128,128,1))

	    inp = inp / 255.0

	    output = model.predict(inp)

	    output = np.argmax(output)

	    if output == 2 and right != False:
	    	pyautogui.click(button="right")
	    	right = False
	    	left = True

	    if output == 3 and left != False:
	    	pyautogui.click(button="left")
	    	left = False
	    	right = True

	    print("+"*50, "\n", output)

	    new_frm = cv2.addWeighted(new_frm ,0.8, mask, 0.2, 0.1)

	    cv2.rectangle(new_frm, (int(x-40), int(y-10)), (int(x+100), int(y+160)), (0,255,0), 2)

	    
	    cv2.imshow("", new_frm)
	    cv2.imshow("drawing", ref)

	    old_gray = new_gray.copy()

	    old_pts = new_pts.reshape(-1,1,2)

	    if key == 27:
	        break


	cv2.destroyAllWindows()
	cap.release()

	return