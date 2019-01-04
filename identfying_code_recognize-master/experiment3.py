import os
import numpy as np
from cv2 import *
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn import  svm
def recognize():
    #讀取數據
    path="C:/Users/fzzf1024/Desktop/train"
    dirs=os.listdir(path)
    # dirs.sort(key=lambda x:int(x[1:-4]))
    data=[]
    for dir in dirs:
        curPath=os.path.join(path,dir);
        curPathsList=os.listdir(curPath);
        for filename in curPathsList:
            img=imread(curPath+'/'+filename,0)
            cv2.threshold(img,140,255,cv2.THRESH_BINARY,dst=img)
            img = cv2.GaussianBlur(img, (7, 7), 0)
            #print(curPath+'/'+filename)
            data.append(img.reshape(1,-1))

    data=np.array(data)
    data.shape=100,-1

    label=[]
    for i in range(10):
        for j in range(10):
            label.append(i)

    #pca降維
    pca=PCA(n_components=15,whiten=True)
    data=pca.fit_transform(data)

    '''调参'''
    '''1<C<e6  0.001<gmmma<0.02 '''
    #gamma_list=np.arange(0.001,0.021,0.002)
    #c_list=[1,10,100,1000,10000]
    gamma_list=[0.017]
    c_list=[10000]

    last_sum_rate=0.0
    for c in c_list:
        for gamma in gamma_list:
            sum_rate=0.0#总正确率
            count = 10#循环计数
            while(count):
                x_train,x_test,y_train,y_test=train_test_split\
                                (data,label,test_size=0.40)
                clf=svm.SVC(C=c,kernel='rbf',gamma=gamma,decision_function_shape='ovo')
                clf.fit(x_train, y_train)
                sum_rate+=clf.score(x_test,y_test)
                count-=1
            if sum_rate>last_sum_rate:
                para1=c;para12=gamma#保存从参数1和参数2
                max_sum_rate=sum_rate#最大正确率之和
                last_sum_rate= sum_rate
    print("C=%d,gamma=%f"%(para1,para12))
    print("正确率%.2f%%"%(max_sum_rate/10*100))

    res=""
    img=imread('CrawlResult/code.png',0)
    cv2.threshold(img, 140, 255, cv2.THRESH_BINARY, dst=img)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    pic1=pca.transform(img[:,11:31].reshape(1,-1))
    res=res+str(int(clf.predict(pic1)))
    pic2=pca.transform(img[:,31:51].reshape(1,-1))
    res=res+str(int(clf.predict(pic2)))
    pic3=pca.transform(img[:,51:71].reshape(1,-1))
    res=res+str(int(clf.predict(pic3)))
    pic4=pca.transform(img[:,71:91].reshape(1,-1))
    res=res+str(int(clf.predict(pic4)))


    print(res)
    return res