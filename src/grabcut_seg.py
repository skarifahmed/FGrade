# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:17:35 2019

@author: Sikha
"""

import numpy as np
import cv2 
#from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\Sikha\Desktop\2.jpg')
denoising_img = cv2.fastNlMeansDenoisingColored(img, None, 11, 11, 7, 15) 
resized_img=cv2.resize(denoising_img,(500,300))
grey_img=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
mask = np.zeros(resized_img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel =np.zeros((1,65),np.float64)
rect = (39,13,370,270)
cv2.grabCut(resized_img,mask,rect,bgdModel,fgdModel,6,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = resized_img*mask2[:,:,np.newaxis]
cv2.imwrite('067.jpg',img)
cv2.imshow("Canny_img",img)
cv2.imshow("canny",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()