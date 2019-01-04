import numpy as np
import cv2
import os
# img=cv2.imread('0.jpg')
index=1
def split(filename,array):
    # print(filename + str(index) + '.jpg')
    global index
    cv2.imwrite(filename + str(index) + '.jpg',array[:,11:31])
    cv2.imwrite(filename + str(index+1) + '.jpg',array[:,31:51])
    cv2.imwrite(filename + str(index+2) + '.jpg',array[:,51:71])
    cv2.imwrite(filename + str(index+3) + '.jpg',array[:,71:91])
    index=index+4
# split('out',img)
# print(index)
path='.//img'
dirs=os.listdir(path)
print(dirs)
for filename in dirs:
    img = cv2.imread(os.path.join(path, filename), 0)
    split(".//splitImgs/",img)


