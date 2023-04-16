import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)
mpg,cyl,disp,hp,drat,wt=data.T
print(mpg)
min=23453453453
max=0
sred=0
c=0
plt.scatter(hp,mpg,s=wt*10)
print(np.min(mpg))
print(np.max(mpg))
print(np.mean(mpg))
for i in range(len(mpg)):
    if(cyl[i]==6):
        if(mpg[i]<min):
            min=mpg[i]
        if(mpg[i]>max):
            max=mpg[i]
        sred+=mpg[i]
        c+=1
print(min,max,(sred/c))
plt.show()