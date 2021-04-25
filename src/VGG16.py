# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:39:34 2020

@author: Sikha
"""

import cv2 
import numpy as np
import glob
import os
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16

input_size=[224,224]
train_image_path='Training_set/'
test_image_path='Testing_set/'

vgg=VGG16(input_shape=input_size + [3], weights='imagenet',include_top=False)

for layer in vgg.layers:
    layer.trainable=False
   
def read_data(path_image):
    array=[]
    label=[]
    folder=os.listdir(path_image)
    for j,out_folder in enumerate(folder):
        image_path=os.path.join(path_image,out_folder)
        image_list=glob.glob(image_path+'/*.jpg')
        for i,image1 in enumerate(image_list):
            img=cv2.imread(image1)
            resize_image=cv2.resize(img,(224,224))
            array.append(resize_image)
            label.append(int(j))
    x=np.asarray(array,dtype='float32')/255.0
    y=np.asarray(label,dtype='int')
    return[x,y]
x_train,y_train=read_data(train_image_path)
x_test,y_test=read_data(test_image_path)

folders=glob('Training_set/*')
x=Flatten()(vgg.output)
prediction=Dense(len(folders),activation='softmax')(x)
model=Model(inputs=vgg.input,outputs=prediction)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=1,batch_size=40,validation_data=(x_test,y_test))