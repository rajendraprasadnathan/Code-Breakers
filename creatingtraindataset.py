# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:55:19 2018

@author: palani
"""

import cv2
import numpy as np
import csv
img1 = cv2.imread('images/c1.jpg');img2 = cv2.imread('images/c2.jpg');img3 = cv2.imread('images/c3.jpg');
img4 = cv2.imread('images/c4.jpg');img5 = cv2.imread('images/c5.jpg');img6 = cv2.imread('images/c6.jpg');
img7 = cv2.imread('images/c7.jpg');img8 = cv2.imread('images/c8.jpg');img9 = cv2.imread('images/c9.jpg');
img10 = cv2.imread('images/c10.jpg');img11 = cv2.imread('images/c11.jpg');img12 = cv2.imread('images/c12.jpg');
img13 = cv2.imread('images/c13.jpg');img14 = cv2.imread('images/c14.jpg');img15 = cv2.imread('images/c15.jpg');
img16 = cv2.imread('images/c16.jpg');img17 = cv2.imread('images/c17.jpg');img18 = cv2.imread('images/c18.jpg');
img19 = cv2.imread('images/c19.jpg');img20 = cv2.imread('images/c20.jpg');img21 = cv2.imread('images/c21.jpg');
img22 = cv2.imread('images/c22.jpg');img23 = cv2.imread('images/c23.jpg');img24 = cv2.imread('images/c24.jpg');
img25 = cv2.imread('images/c25.jpg');img26 = cv2.imread('images/c26.jpg');img27 = cv2.imread('images/c27.jpg');
img28 = cv2.imread('images/c28.jpg');img29 = cv2.imread('images/c29.jpg');img30 = cv2.imread('images/c30.jpg');
img31 = cv2.imread('images/c31.jpg');img32 = cv2.imread('images/c32.jpg');img33 = cv2.imread('images/c33.jpg');
img34 = cv2.imread('images/c34.jpg');img35 = cv2.imread('images/c35.jpg');img36 = cv2.imread('images/c36.jpg');
img37 = cv2.imread('images/c37.jpg');img38 = cv2.imread('images/c38.jpg');img39 = cv2.imread('images/c39.jpg');
img40 = cv2.imread('images/c40.jpg');img41 = cv2.imread('images/c41.jpg');img42 = cv2.imread('images/c42.jpg');
img43 = cv2.imread('images/c43.jpg');img44 = cv2.imread('images/c44.jpg');img45 = cv2.imread('images/c45.jpg');
img46 = cv2.imread('images/c46.jpg');img47 = cv2.imread('images/c47.jpg');img48 = cv2.imread('images/c48.jpg');
img49 = cv2.imread('images/c49.jpg');img50 = cv2.imread('images/c50.jpg')
resized_image1 = cv2.resize(img1, (50, 50)); resized_image2 = cv2.resize(img2, (50, 50));
resized_image3 = cv2.resize(img3, (50, 50));resized_image4 = cv2.resize(img4, (50, 50));
resized_image5 = cv2.resize(img1, (50, 50));resized_image6 = cv2.resize(img6, (50, 50));
resized_image7 = cv2.resize(img7, (50, 50));resized_image8 = cv2.resize(img8, (50, 50));
resized_image9 = cv2.resize(img9, (50, 50));resized_image10 = cv2.resize(img10, (50, 50));
resized_image11 = cv2.resize(img11, (50, 50));resized_image12 = cv2.resize(img12, (50, 50));
resized_image13 = cv2.resize(img13, (50, 50));resized_image14 = cv2.resize(img14, (50, 50));
resized_image15 = cv2.resize(img15, (50, 50));resized_image16 = cv2.resize(img16, (50, 50));
resized_image17 = cv2.resize(img17, (50, 50));resized_image18 = cv2.resize(img18, (50, 50));
resized_image19 = cv2.resize(img19, (50, 50));resized_image20 = cv2.resize(img20, (50, 50));
resized_image21 = cv2.resize(img21, (50, 50));resized_image22 = cv2.resize(img22, (50, 50));
resized_image23 = cv2.resize(img1, (50, 50));resized_image24 = cv2.resize(img24, (50, 50));
resized_image25 = cv2.resize(img25, (50, 50));resized_image26 = cv2.resize(img26, (50, 50));
resized_image27 = cv2.resize(img27, (50, 50));resized_image28 = cv2.resize(img28, (50, 50));
resized_image29 = cv2.resize(img29, (50, 50));resized_image30 = cv2.resize(img30, (50, 50));
resized_image31 = cv2.resize(img31, (50, 50));resized_image32 = cv2.resize(img32, (50, 50));
resized_image33 = cv2.resize(img33, (50, 50));resized_image34 = cv2.resize(img34, (50, 50));
resized_image35 = cv2.resize(img35, (50, 50));resized_image36 = cv2.resize(img36, (50, 50));
resized_image37 = cv2.resize(img37, (50, 50));resized_image38 = cv2.resize(img38, (50, 50));
resized_image39 = cv2.resize(img39, (50, 50));resized_image40 = cv2.resize(img40, (50, 50));
resized_image41 = cv2.resize(img41, (50, 50));resized_image42 = cv2.resize(img42, (50, 50));
resized_image43 = cv2.resize(img43, (50, 50));resized_image44 = cv2.resize(img44, (50, 50));
resized_image45 = cv2.resize(img45, (50, 50));resized_image46 = cv2.resize(img46, (50, 50));
resized_image47 = cv2.resize(img47, (50, 50));resized_image48 = cv2.resize(img48, (50, 50));
resized_image49 = cv2.resize(img49, (50, 50));resized_image50 = cv2.resize(img50, (50, 50));
imgray1 = cv2.cvtColor(resized_image1, cv2.COLOR_BGR2GRAY);imgray2 = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY);
imgray3 = cv2.cvtColor(resized_image3, cv2.COLOR_BGR2GRAY);imgray4 = cv2.cvtColor(resized_image4, cv2.COLOR_BGR2GRAY);
imgray5 = cv2.cvtColor(resized_image5, cv2.COLOR_BGR2GRAY);imgray6 = cv2.cvtColor(resized_image6, cv2.COLOR_BGR2GRAY);
imgray7 = cv2.cvtColor(resized_image7, cv2.COLOR_BGR2GRAY);imgray8 = cv2.cvtColor(resized_image8, cv2.COLOR_BGR2GRAY);
imgray9 = cv2.cvtColor(resized_image9, cv2.COLOR_BGR2GRAY);imgray10 = cv2.cvtColor(resized_image10, cv2.COLOR_BGR2GRAY);
imgray11 = cv2.cvtColor(resized_image11, cv2.COLOR_BGR2GRAY);imgray12 = cv2.cvtColor(resized_image12, cv2.COLOR_BGR2GRAY);
imgray13 = cv2.cvtColor(resized_image13, cv2.COLOR_BGR2GRAY);imgray14 = cv2.cvtColor(resized_image14, cv2.COLOR_BGR2GRAY);
imgray15 = cv2.cvtColor(resized_image15, cv2.COLOR_BGR2GRAY);imgray16 = cv2.cvtColor(resized_image16, cv2.COLOR_BGR2GRAY);
imgray17 = cv2.cvtColor(resized_image17, cv2.COLOR_BGR2GRAY);imgray18 = cv2.cvtColor(resized_image18, cv2.COLOR_BGR2GRAY);
imgray19 = cv2.cvtColor(resized_image19, cv2.COLOR_BGR2GRAY);imgray20 = cv2.cvtColor(resized_image20, cv2.COLOR_BGR2GRAY);
imgray21 = cv2.cvtColor(resized_image21, cv2.COLOR_BGR2GRAY);imgray22 = cv2.cvtColor(resized_image22, cv2.COLOR_BGR2GRAY);
imgray23 = cv2.cvtColor(resized_image23, cv2.COLOR_BGR2GRAY);imgray24 = cv2.cvtColor(resized_image24, cv2.COLOR_BGR2GRAY);
imgray25 = cv2.cvtColor(resized_image25, cv2.COLOR_BGR2GRAY);imgray26 = cv2.cvtColor(resized_image26, cv2.COLOR_BGR2GRAY);
imgray27 = cv2.cvtColor(resized_image27, cv2.COLOR_BGR2GRAY);imgray28 = cv2.cvtColor(resized_image28, cv2.COLOR_BGR2GRAY);
imgray29 = cv2.cvtColor(resized_image29, cv2.COLOR_BGR2GRAY);imgray30 = cv2.cvtColor(resized_image30, cv2.COLOR_BGR2GRAY);
imgray31 = cv2.cvtColor(resized_image31, cv2.COLOR_BGR2GRAY);imgray32 = cv2.cvtColor(resized_image32, cv2.COLOR_BGR2GRAY);
imgray33 = cv2.cvtColor(resized_image33, cv2.COLOR_BGR2GRAY);imgray34 = cv2.cvtColor(resized_image34, cv2.COLOR_BGR2GRAY);
imgray35 = cv2.cvtColor(resized_image35, cv2.COLOR_BGR2GRAY);imgray36 = cv2.cvtColor(resized_image36, cv2.COLOR_BGR2GRAY);
imgray37 = cv2.cvtColor(resized_image37, cv2.COLOR_BGR2GRAY);imgray38 = cv2.cvtColor(resized_image38, cv2.COLOR_BGR2GRAY);
imgray39 = cv2.cvtColor(resized_image39, cv2.COLOR_BGR2GRAY);imgray40 = cv2.cvtColor(resized_image40, cv2.COLOR_BGR2GRAY);
imgray41 = cv2.cvtColor(resized_image41, cv2.COLOR_BGR2GRAY);imgray42 = cv2.cvtColor(resized_image42, cv2.COLOR_BGR2GRAY);
imgray43 = cv2.cvtColor(resized_image43, cv2.COLOR_BGR2GRAY);imgray44 = cv2.cvtColor(resized_image44, cv2.COLOR_BGR2GRAY);
imgray45 = cv2.cvtColor(resized_image45, cv2.COLOR_BGR2GRAY);imgray46 = cv2.cvtColor(resized_image46, cv2.COLOR_BGR2GRAY);
imgray47 = cv2.cvtColor(resized_image47, cv2.COLOR_BGR2GRAY);imgray48 = cv2.cvtColor(resized_image48, cv2.COLOR_BGR2GRAY);
imgray49 = cv2.cvtColor(resized_image49, cv2.COLOR_BGR2GRAY);imgray50 = cv2.cvtColor(resized_image50, cv2.COLOR_BGR2GRAY);
print(imgray1.shape)
x=[]
image1=[];image2=[]; image3=[]; image4=[]; image5=[]; image6=[];image7=[] ;
image8=[] ;image9=[];image10=[];image11=[];image12=[];image13=[];
image14=[];image15=[];image16=[];image17=[];image18=[];image19=[];image20=[];
image21=[];image22=[];image23=[];image24=[];image25=[];image26=[];
image27=[];image28=[];image29=[];image30=[];image31=[];image32=[];image33=[];
image34=[];image35=[];image36=[];image37=[];image38=[];image39=[];image40=[];image41=[];
image42=[];image43=[];image44=[];image45=[];image46=[];image47=[];image48=[];
image49=[];image50=[];
y=[x,image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,
   image11,image12,image13,image14,image15,image16,image17,image18,image19,image20,
   image21,image22,image23,image24,image25,image26,image27,image28,image29,image30,
   image31,image32,image33,image34,image35,image36,image37,image38,image39,image40,
   image41,image42,image43,image44,image45,image46,image47,image48,image49,image50]
for i in range(0,2500):
    x.append(str(("PIXEL")+str(" ")+str(i)))
for row in range(0,50):
    for column in range(0,50):
        image1.append(imgray1[row,column]);image2.append(imgray2[row,column]);
        image3.append(imgray3[row,column]);image4.append(imgray4[row,column]);
        image5.append(imgray5[row,column]);image6.append(imgray6[row,column]);
        image7.append(imgray7[row,column]);image8.append(imgray8[row,column]);
        image9.append(imgray9[row,column]);image10.append(imgray10[row,column]);
        image11.append(imgray11[row,column]);image12.append(imgray12[row,column]);
        image13.append(imgray13[row,column]);image14.append(imgray14[row,column]);
        image15.append(imgray15[row,column]);image16.append(imgray16[row,column]);
        image17.append(imgray17[row,column]);image18.append(imgray18[row,column]);
        image19.append(imgray19[row,column]);image20.append(imgray20[row,column]);
        image21.append(imgray21[row,column]);image22.append(imgray22[row,column]);
        image23.append(imgray23[row,column]);image24.append(imgray24[row,column]);
        image25.append(imgray25[row,column]);image26.append(imgray26[row,column]);
        image27.append(imgray27[row,column]);image28.append(imgray28[row,column]);
        image29.append(imgray29[row,column]);image30.append(imgray30[row,column]);
        image31.append(imgray31[row,column]);image32.append(imgray32[row,column]);
        image33.append(imgray33[row,column]);image34.append(imgray34[row,column]);
        image35.append(imgray35[row,column]);image36.append(imgray36[row,column]);
        image37.append(imgray37[row,column]);image38.append(imgray38[row,column]);
        image39.append(imgray39[row,column]);image40.append(imgray40[row,column]);
        image41.append(imgray41[row,column]);image42.append(imgray42[row,column]);
        image43.append(imgray43[row,column]);image44.append(imgray44[row,column]);
        image45.append(imgray45[row,column]);image46.append(imgray46[row,column]);
        image47.append(imgray47[row,column]);image48.append(imgray48[row,column]);
        image49.append(imgray49[row,column]);image50.append(imgray50[row,column]);
with open('datapaper.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(y)
writeFile.close()