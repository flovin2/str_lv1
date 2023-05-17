import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')
print((mtcars.sort_values(by=['mpg']).head(5)))
print((mtcars[mtcars.cyl==8].sort_values(by=['mpg'],ascending=False).head(3)))
print(mtcars.query('cyl==6').mpg.mean())
print("4.")
print(mtcars[(mtcars.cyl==4) & (mtcars.wt<2.200) & (mtcars.wt>2.000)].mpg)
print(mtcars[mtcars.am==0].car.count())
print(mtcars[mtcars.am==1].car.count())
print(mtcars[(mtcars.am==1) & (mtcars.hp>100)])
print(mtcars.wt * 1000 * 0.45359237)
