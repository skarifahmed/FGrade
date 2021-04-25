# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:16:20 2020

@author: Sikha
"""

import cv2
import glob
import numpy as np
from PIL import Image
import os
#Boundary Cropped
files =glob.glob('seg_images/**/*.*')
for file in files:
    #im=Image.open(file)
    im=cv2.imread(file)
    h,w,_=im.shape
    for i in range(h):
        for j in range(w):
            if im[i,j,0]<=15 and im[i,j,1]<=15 and im[i,j,2]<=15:
                im[i,j,0]=0
                im[i,j,1]=0
                im[i,j,2]=0
    sm=np.sum(im[:,:,0],axis=0)
    for i,k in enumerate(sm):
        if k==0:
            continue
        else:
            L=i-1
            break
    for i,k in enumerate(sm[::-1]):
        if k==0:
            continue
        else:
            R=500-i-1
            break
    sm=np.sum(im[:,:,0],axis=1)
    for i,k in enumerate(sm):
        if k==0:
            continue
        else:
            T=i-1
            break
    for i,k in enumerate(sm[::-1]):
        if k==0:
            continue
        else:
            B=300-i-1
            break
    I=Image.open(file)
    img=I.crop((L,T,R,B))
    #img1=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    #img.show()
    k='out_2/'+file.split('.')[0][:-3]
    if not os.path.isdir(k):
       os.makedirs(k)
    img.save(k+file.split('\\')[-1])
    #cv2.imwrite(k+file.split('\\')[-1],img1)
    print(file)
#files=glob.glob('out/*.*')
#change background black to white
files =glob.glob('seg_images/**/*.*')    
for file in files:
    im=cv2.imread(file)
    h,w,_=im.shape
    for i in range(h):
        for j in range(w):
            if im[i,j,0]<=42 and im[i,j,1]<=42 and im[i,j,2]<=42:
                im[i,j,0]=255
                im[i,j,1]=255
                im[i,j,2]=255
                
    k='out3/'+file.split('.')[0][:-3]
    if not os.path.isdir(k):
        os.makedirs(k)
    cv2.imwrite(k+file.split('\\')[-1],im)
    print(file)