# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 17:40:44 2018

@author: palani
"""
import numpy as np
import cv2
import csv
import matplotlib.pyplot as pt
import pandas as pd
import requests
import time
last_update_time = time.time()
cap = cv2.VideoCapture('http://192.168.43.1:8080/shot.jpg') # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('images/c56.jpg',frame)
        cv2.destroyAllWindows()
        break
cap.release()
img = cv2.imread('images/c56.jpg')
resized_image1 = cv2.resize(img, (50, 50)) 
imgray1 = cv2.cvtColor(resized_image1, cv2.COLOR_BGR2GRAY)
image1=[]
image2=[]
x=[image1,image2]
for row in range(0,50):
    for column in range(0,50):
        image1.append(imgray1[row,column])
        image2.append(imgray1[row,column])
image1.append(100)
image2.append(150)

with open('data.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(x)
writeFile.close()
from sklearn.tree import DecisionTreeClassifier
data =pd.read_csv("maintrain.csv").as_matrix()
data1=pd.read_csv("data.csv").as_matrix()
clf = DecisionTreeClassifier()
xtrain = data[0:100, 1:]
train_label = data[0:100, 0]
clf.fit(xtrain, train_label)
xtest = data1[0:, 1:]
actual_label= data1[1:, 0]
print(len(xtest))
d = xtest[0]
y=clf.predict([xtest[0]])
print (y)
if(time.time()-last_update_time)>5:
    if(y==['Paper']):
        r=requests.get("http://api.thingspeak.com/update?api_key=L2N55U1O9187NUFJ&field1="+str(1)+"&field2="+str(0))
        print (r.content)
        print("updating to thingspeak")
        last_update_time = time.time()
        time.sleep(1)
    elif(y==['Plastic']):
        r=requests.get("http://api.thingspeak.com/update?api_key=L2N55U1O9187NUFJ&field1="+str(0)+"&field2="+str(1))
        print (r.content)
        print("updating to thingspeak")
        last_update_time = time.time()
        time.sleep(1)
    else:
        r=requests.get("http://api.thingspeak.com/update?api_key=L2N55U1O9187NUFJ&field1="+str(0)+"&field2="+str(0))
        print (r.content)
        print("updating to thingspeak")
        last_update_time = time.time()
        time.sleep(1)
        
        
    