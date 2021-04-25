# -*- coding: utf-8 -*-
"""
Created on Fri May 15 06:39:17 2020

@author: Sikha
"""
import cv2
from keras.models import model_from_json
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import numpy as np
from keras.utils import to_categorical
import os
import glob
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
array=[]
path_image='Test_10/'
def Read_data(path_image):
    array=[]
    label=[]
    folder=os.listdir(path_image)
    for j,out_folder in enumerate(folder):
        image_path=os.path.join(path_image,out_folder)
        image_list=glob.glob(image_path+'/*.jpg')
        for i,image in enumerate(image_list):
                img=cv2.imread(image)
                resize_image=cv2.resize(img,(224,224))
                array.append(resize_image)
                label.append(int(j))
    x_test=np.asarray(array,dtype='float32')/255.0
    y_test=np.asarray(label,dtype='int')
   # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.10,random_state=4)
    yy_test=y_test.copy()
    y_test=to_categorical(y_test)
    return x_test,y_test,yy_test
##Read the single image
#def single_image():
#    img = cv2.imread(r'C:\Users\Sikha\Desktop\16.jpg')
#    resized_img=cv2.resize(img,(128,128))
#    array.append(resized_img)
#    x=np.asarray(array,dtype='float32')/255.0
#    return x

# load json and create model
def reload():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("ckpt.h5")
    loaded_model.summary()
    return loaded_model
#check the accuracy 
def Score():
    X_test,Y_test,YY_test=Read_data(path_image)
    loaded_model=reload()
    Y_pred=loaded_model.predict(X_test).argmax(axis=1)
    score=accuracy_score(YY_test,Y_pred)
    print("Classification Reports:\n",classification_report(Y_test,Y_pred))
    print('Accuracy=',score)
    con_matrix=confusion_matrix(YY_test,Y_pred)
    print('Confusion Matrix:\n',con_matrix)
   
Score()
