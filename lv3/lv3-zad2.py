import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')
plt.figure()
cylm= pd.DataFrame({'cylm':[4,6,8], 'val':[mtcars[mtcars.cyl==4].mpg.mean(),mtcars[mtcars.cyl==6].mpg.mean(),mtcars[mtcars.cyl==8].mpg.mean()]})
potr= pd.DataFrame({'vrsta':['r','a'], 'mpg':[mtcars[mtcars.am==0].mpg.mean(),mtcars[mtcars.am==1].mpg.mean()]})
ubrz=pd.DataFrame({'vrsta':['r','a'],'hp':[mtcars.hp],'qsec':[mtcars.qsec]})

#cylm.plot.bar(x='cylm',y='val')
#mtcars.plot.box(column='wt',by='cyl')
#potr.plot.bar(x='vrsta',y='mpg')
ubrz.plot.bar(x='hp',y='qsec',color={'r':'green','a':'red'})
plt.show()
