import scipy.signal as sig
import numpy as np
import borda
import binary
import cv2



def main():

	cv2.namedWindow("Vizualization 1")
	cv2.namedWindow("Vizualization 2")
	vc = cv2.VideoCapture(0)
	green = np.array([0, 255, 0])

	if vc.isOpened():
		rval, frame = vc.read()
	else:
		rval = False

	while rval:

		gray = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
		g = binary.main(gray)
		ed = borda.edge(g)
		ed = np.array(cv2.cvtColor(ed, cv2.COLOR_GRAY2BGR)) #
		
		out = cv2.addWeighted(frame, 0.5, ed, 0.5, 0)
		cv2.imshow("Vizualization 1", out)
		cv2.imshow("Vizualization 2", ed)
		rval, frame = vc.read()
		key = cv2.waitKey(20)
		if key == 27:
			break

	cv2.destroyAllWindows()



if __name__ == "__main__":
	main()