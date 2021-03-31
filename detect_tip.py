import cv2
import numpy as np

def detect_tip():
	cap = cv2.VideoCapture(0)

	net = cv2.dnn.readNetFromCaffe("pose_deploy.prototxt", "pose_iter_102000.caffemodel")

	while True:
		_, frame = cap.read()
		frame= cv2.flip(frame, 1)

		cv2.imshow("window", frame)

		if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			break

	inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (640, 480),(0, 0, 0), swapRB=False, crop=False)

	net.setInput(inpBlob)
		 
	output = net.forward()

	probMap = output[0, 8, :, :]
	probMap = cv2.resize(probMap, (640, 480))
    
	minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

	#if prob > 0.5 :
		#cv2.circle(frame, (int(point[0]), int(point[1])), 2, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
		#cv2.putText(frame, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

	#cv2.imshow("window", frame)
	#cv2.waitKey(0)
	cap.release()
	return point, frame