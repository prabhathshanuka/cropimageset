#import the library opencv
import cv2
#globbing utility.
import glob
import numpy as np
#select the path
#I have provided my path from my local computer, please change it accordingly

def imagecrop():
	img = a
	

 
	print('Original Dimensions : ',img.shape)
 
	scale_percent = 20 # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
	print('Resized Dimensions : ',resized.shape)

 
	#cv2.imshow("Resized image", resized)
	#cv2.waitKey(0)
	y= "D:/mytoolspython/croped/" +(x)+".png"
	r = cv2.selectROI(resized)
	crop_img = resized[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
	img = crop_img
	cv2.imshow("croped", crop_img)

	cv2.waitKey(0)
	cv2.imwrite(y,img) 
	cv2.waitKey(0)
	cv2.destroyAllWindows()


path = "C:/Users/shanuka/Desktop/java\*.*"
for file in glob.glob(path):
    #print(file)
    x = str(input("Enter a number: "))
	
    a= cv2.imread(file)
	
    #print(a)
    imagecrop()

    # %%%%%%%%%%%%%%%%%%%%%
    #conversion numpy array into rgb image to show
    #c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    #cv2.imshow('Color image', c)
    #wait for 1 second


    k = cv2.waitKey(100)
    #destroy the window
    cv2.destroyAllWindows()


    # %%%%%%%%%%%%%%%%%%%%%





