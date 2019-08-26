#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:33:21 2019

@author: pawan
"""
''' Variables and Strings'''
#%%
print("Hello World")




#%%


message="hi!"
print(message.capitalize())

type(message)

#%%
'''Replace'''

sister="Liz"
print(sister)
print(sister.replace("z","sa"))



#%%
print("DESSERTS")

#%%

x=5
y=10
print(x+y)

#%%
k="5"
m="6"
print(k+m)

#%%

#%%

f=input("First Name      ")
l=input("Last Name      ")
full_name=f+" "+l
print(full_name)

#%%
'''Lists'''
Department =['SES','SBS','SEOCS','SIF','SMS']

print(Department[0])
print(Department[-1])


#%%
'''Index'''


print(Department.index('SEOCS'))

#%%

full="STRESSED"
full[::-1]

#%%
'''Slicing''' 

roll_no=[1,2,3,4,5,6]
print(x[2])
print(x[2:4])
print(x[2 :-2])
#%%
'''Changing List Element'''
list=[2,25,8,45,63,45,85]
list[2]=5
print(list)


#%%

'''Extending A List '''
list1=list+[23,12,78]
print(list1)


#%%
'''Adding Element using append'''
list2=[23,46,79]
list2.append(45)
print(list2)




#%%
'''Statements  &  Loops'''

marks=int(input("Your Marks"))
if marks>= 30:
    print("Qualified")
else:
    print("Don't Giveup")
    
    
    
#%%
    '''for loop'''
    
for i in range (25):
    print(i)

#%%
squares=[]
for i in range(10):
    square=i**2
    squares.append(square)
print(squares)    

    

#%%
square=[j**2 for j in range(10)]
print(square)


#%%
'''Dictionary'''
Class={"XYZ":25,"ABC":12,"KLM":{"TUV":98}}
print(Class["KLM"]["TUV"])

#%%
'''Check if it's there or not'''


"KLM" in Class
#%%
'''Delete it '''

del(Class["KLM"])
print(Class)


#%%
'''Pandas'''
import pandas pd

file=pd.read_csv('')





#%%%
'''Function'''
def make_pizza(name='namethepizza'):
    take=input("Name the pizza you want to cook    ")
    print("Have a " + take + " pizza!")


#%%
 '''Array Multiplication'''
   
x=[1,2,3,4,5]
x*5


#&&
'''Numpy'''

import numpy as np
y=np.array([1,2,3,4,5])
z=y**2
print(z)
#%%
'''MAX'''

max=np.max(z)
print(max)
#%%
'''Square root'''

print(np.sqrt(max))

#%%
'''Mean'''

mean=np.mean(z)
print(mean)
#%%

'''Median'''
median=np.median(z)

print(median)


#%%

'''Matplotlib'''
import matplotlib.pyplot as plt 

h=[21,2,86,36,45,75,52,65,42,52,78,37,46,83,15,68,46]
plt.hist(h,bins=10)



#%%
plt.plot(h,marker='o')


#%%


plt.scatter()

#%%
'''Basemap'''
from mpl_toolkits.basemap import Basemap
m=Basemap(projection='mill',llcrnrlat=4.125,urcrnrlat=23.875,llcrnrlon=76.125,urcrnrlon=99.875,resolution='h')
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary()
m.fillcontinents()
m.drawrivers(color='aqua')
m.drawparallels(np.array([4,6,8,10,12,14,16,18,20,22,24]),labels=[1,0,0,0],linewidth='0.1',fontsize='8')
m.drawmeridians(np.array([76,79,82,85,88,91,94,97,99]),labels=[0,0,0,1],linewidth='0.1',fontsize='8')
x,y=np.meshgrid(blon,blat)
X,Y=m(x,y)
#plt.contourf(X,Y,ssha1[:,:].T,70,cmap='jet')
#plt.colorbar()
plt.quiver(X,Y,ug,vg,pivot='middle',color='k', width=0.0009 , scale=50, alpha = 0.95 ,headwidth = 6)
#plt.annotate('Odisha', xy=(0.27, 0.8), xycoords='axes fraction',color='r')
QV1=plt.quiver(X[5][19],Y[5][19],1,0,pivot='middle',color='r', width=0.0009 , scale=50, alpha = 1, headwidth = 9)

plt.annotate('1 m/s',xy=(0.16,0.025),xycoords='axes fraction',color='r',fontsize=6)
plt.title('SSHA + Geostrophic Current: 15-May-2017')
plt.quiverkey(QV1,X=1.05, Y=1.03,U=1, label='1 m/s', labelpos='E')
plt.show()

#%%



