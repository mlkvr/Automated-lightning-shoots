# program to capture lighning moments from webcam in python

# importing OpenCV library and Numpy
import cv2
import numpy as np

# initialize the camera
vid = cv2.VideoCapture(1)

# for naming ordered photos
counter=0

while (True):

	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
  
  # Turn BGR image to HSV 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  # We are interested in Value so split HSV 
	hsv_planes = cv2.split(hsv)
	v_hist = cv2.calcHist(hsv_planes, [2], None, [256], (0, 256), accumulate=False)
	
  # Lower = Brighter
	if(v_hist[0]<100):
		cv2.imwrite(f"{counter}.png", frame)
		counter = counter + 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
