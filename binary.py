import scipy.signal as sig 
import numpy as np 
import cv2



def histogram(inImage):

	inten = np.unique(inImage)
	freqs = np.zeros_like(inten)

	for i in range(len(inten)):
		freqs[i] = np.array(inImage == inten[i]).sum()

	return inten, freqs



def findThresh(inImage):
	
	output = np.zeros_like(inImage)
	inten, freqs = histogram(inImage)

	l1 = np.mean(inten)
	l0 = np.zeros_like(inten[0])
	dif = np.abs(l1-l0)

	while dif > 0.00001:
		l0 = l1
		idx = (inten >= l1)
		m1 = np.mean(inten[idx])
		m2 = np.mean(inten[~idx])
		l1 = np.float_((m1 + m2)/2)
		dif = np.abs(l1-l0)

	output = 255*(inImage >= l1)

	return np.uint8(output)


def main(inImage):
	
	#n = input("Fale o numero de contornos: ")
	output = findThresh(inImage)

	return output



# if __name__ == "__main__":
# 	main()
