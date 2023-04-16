import numpy as np
import matplotlib.pyplot as plt

def kvadratna_slika(velicina,broj_wid,broj_height):
     black=np.zeros((velicina,velicina))
     white=np.ones((velicina,velicina))
     
     res=black
     res2=white
     res3=white
     res4=black
     for i in range (1,broj_wid):     
         res=np.hstack((res,res2))
         res3=np.hstack((res3,res4))        
         if(i%2!=0):
            res2=black
            res4=white
         if(i%2==0):
            res2=white
            res4=black
     res2=res3
     res4=res

     for i in range(1,broj_height):
        res=np.vstack((res,res2))
        if(i%2!=0):
            res2=res4
              
        if(i%2==0):
            res2=res3
     return res

res=kvadratna_slika(50,6,4)

plt.figure()
plt.imshow(res,cmap='RdBu_r')
plt.show()  