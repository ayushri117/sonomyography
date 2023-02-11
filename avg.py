import cv2
import os
import glob
import numpy as np
for dir in glob.glob("Ayush_us_data/train/*"):
    counter=1
    for img_name in os.listdir(dir):
        path=os.path.join(dir,img_name)
        img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img=np.array(img)
        if(counter==1):
            avg=img
        else:
            avg=avg*((counter-1)/counter) +(img)*(1/counter)
        counter+=1
    avg=np.uint8(avg)
    cv2.imwrite(f"{dir}.jpg",avg)
