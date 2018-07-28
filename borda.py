import scipy.signal as sig
import numpy as np
import cv2



def erosion(inImage, w):
	lim1 = inImage.shape[0] - 1;
	lim2 = inImage.shape[1] - 1;
	l = (w.shape[1]-1)/2

	output = np.zeros_like(inImage)

	for i in range(1,lim1):
		for j in range(1,lim2):

			if w.sum() == inImage[(i-l):(i+l+1), (j-l):(j+l+1)].sum():	
				output[i][j] = 255

	return np.uint8(output)



def edge(inImage):
	inFact = 3
	# inP = './imagens/blob.png'
	# inImage = cv2.imread(inP)
	# inImage = np.array(cv2.cvtColor(inImage, cv2.COLOR_BGR2GRAY))

	w = 255*np.ones_like(inImage[0:inFact,0:inFact])
	output = erosion(inImage, w)
	output = inImage - output

	# cv2.imshow('Original', inImage)
	# cv2.imshow('Borders', output)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	return output

# if __name__ == "__main__":
# 	inImage = np.array(cv2.imread('photo'))
# 	edge(imImage)