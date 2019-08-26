#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:02:30 2019

@author: pawan
"""
#%%
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from netCDF4 import Dataset
import netCDF4
file=Dataset('/home/pawan/Documents/Parcels/GHRSST/8151FDDD3AC3C97E91F46B6E03CC7FD8_ferret_listing.nc')
file.variables
lon=np.array(file['LON5121_5600'])
lat=np.array(file['LAT1881_2280'])
SST=np.array(file['SST'])
SST1=SST[0,:,:]

SST1[(SST1>50)]=np.nan
#plt.contourf(lon,lat,SST1)
m=Basemap(projection='mill',llcrnrlat=4.125,urcrnrlat=23.875,llcrnrlon=76.125,urcrnrlon=99.875,resolution='h')
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary()
m.fillcontinents()
x,y=np.meshgrid(lon,lat)
X,Y=m(x,y)
plt.contourf(X,Y,SST1,100,cmap='jet')
plt.colorbar()
