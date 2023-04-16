import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img = img[:,:,0].copy()
e=img
img=img*2
for i in range(len(img)):
    for j in range(len(img[0])):    
        if(img[i][j]>1):
            img[i][j]=1
b=np.zeros((960,640))
c=np.zeros((640,960))
d=img[::5,::5]
   
#img=img[0:960,:img.shape[1]]


for i in range(0,img.shape[0]):
    b[:,img.shape[0]-1-i]=img[i,:]
for i in range(0,img.shape[1]):
    c[:,img.shape[1]-1-i]=img[:,i]       

h=(int)(e.shape[1]*1/4)
e[:,:h]=0
e[:,h*2:e.shape[1]]=0


print(img.dtype)
plt.figure()
#imshow first argument is img for a),b for b), c for c), d for d), e for e)
plt.imshow(b,cmap='gray')
plt.show()  


     