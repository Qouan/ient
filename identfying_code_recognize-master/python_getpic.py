import requests
import os

path='C:/Users/fzzf1024/Desktop/identfying_code_recognize-master/img//'
num=100
if os.path.exists(path):  

    pass
else:

    os.makedirs(path)
for i in range(0,num):
    print("下载第"+str(i)+"张验证码")
    filePath=path+str(i)+'.jpg'
    #这个地址下可以下载到普通的验证码
    r=requests.get('https://zfw.xidian.edu.cn//site/captcha?v=5c10e76c6a653')
    with open(filePath,'bw') as f:
        f.write(r.content)
    
