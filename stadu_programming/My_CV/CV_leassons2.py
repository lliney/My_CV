import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imutils

image=cv2.imread('matplotlib-rgb-fixed.jpg')
plt.axis('off')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

#im=im[:200,:100,]
#print(im.shape)
#imgreen=im[:,:,1]
#a=np.array(imgreen)
#print(a.shape)
#imgreen=imgreen[:150,:100]
#print(imgreen.shape)
#imgrad=im[:,:,0]
#imgblue=im[:,:,2]
#cv2.imshow('image',im)
#cv2.imshow('img',im)
##cv2.imshow('blue',imgblue)
#cv2.waitKey(0)