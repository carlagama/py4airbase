# -*- coding: utf-8 -*-

# carlagama@ua.pt
# 2015.02.23

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# load list of AirBase stations (previously downloaded from
# http://www.eea.europa.eu/data-and-maps/data/airbase-the-european-air-quality-database-8)
d = pd.read_table('AirBase_v8_stations.csv')

lons = d['station_longitude_deg']
lats = d['station_latitude_deg']

# draw map with markers for float locations
m = Basemap(resolution='i')
x, y = m(lons,lats)
m.fillcontinents(color='0.95', lake_color='0.95', zorder=-10)
m.drawcountries(linewidth = 0.5, zorder=-1)
#m.drawcoastlines(linewidth=0.5)
for j,cp in enumerate(m.coastpolygons):
    if m.coastpolygontypes[j]<2:
        m.plot(cp[0],cp[1],'k-', linewidth=0.5, zorder=-1)

m.scatter(x,y,s=2, marker='o',color='DarkOrange')

plt.title('Locations of the AirBase stations',fontsize=12)
plt.show()
