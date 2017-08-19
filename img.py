import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

	success,image = cap.read()
	count = 0
	success = True
	while success:
		success,image = cap.read()
		print('Read a new frame: ', success)
		cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
		count += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

