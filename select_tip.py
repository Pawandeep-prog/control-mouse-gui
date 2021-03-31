import cv2
import numpy as np

x1, y1 = -1, -1
k = -1
def select_tip():
	global x1, y1, k
	flag = True

	cap = cv2.VideoCapture(0)

	def draww(event, x, y, flag, param):
	    global x1, y1, k
	    if event == cv2.EVENT_LBUTTONDOWN:
	        x1 = x
	        y1 = y
	        k = 1


	cv2.namedWindow("img")
	cv2.setMouseCallback("img", draww)

	while True:
		_, selec = cap.read()
		selec = cv2.flip(selec, 1)
		old_gray = cv2.cvtColor(selec, cv2.COLOR_BGR2GRAY)
		cv2.imshow("img", selec)
		if k == 1 or cv2.waitKey(1) == 27:
			k = -1
			cv2.destroyAllWindows()
			break


	old_pts = [x1, y1]
	cap.release()

	return old_pts, selec
