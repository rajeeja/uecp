#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 18:27:44 2016
#This file creates utm coordinates from geojson 
@author: rajeevjain
"""

import sys
import utm
import math
import geojson
import json
from pprint import pprint
import os

vcount = 0
scount = 0
xmin = -1e8
xmax = 1e8
ymin = -1e8
ymax = 1e8
zmax = -1

def cartesian(lon,lat, elevation):
    R = 6378137.0 + elevation  # relative to centre of the earth
    x = R * math.cos(lat) * math.cos(lon)
    y = R * math.cos(lat) * math.sin(lon)
    z = R * math.sin(lat)
    print ("create vertex ", x, y, z, file=jou)      
    return X, Y, Z
 
    
scheme = 1
    
#with open('1bldg_fed_irs.geojson') as f:
#with open('2bldg_fed.geojson') as f:    
#with open('4blocks_all_bldg.geojson') as f: 
file = sys.argv[1]
ifile = sys.argv[1] + ".geojson"
ofile = sys.argv[1] + ".jou"
bfile = sys.argv[1] + ".txt"

if os.path.exists(ofile):
    os.remove(ofile)
if os.path.exists(bfile):
    os.remove(bfile)    
jou = open(ofile, "a")    
bld = open(bfile, "a")    

with open(ifile) as f:          
    data = json.load(f)
height = []
msurf_list = []
print("\nreset", file = jou)
for feature in data['features']:
    i = 0
    j = 0
    print ("# ", feature['geometry']['type'])
    print ("# ", feature['properties']['bldg_name1'])
    print ("# ", feature['properties']['bldg_name2'])
    floor = feature['properties']['stories']

    height.append(floor*3.0)
  #  print ("# height ", height)
  #  print ("# building id", feature['properties']['bldg_id'])
    a = feature['geometry']['coordinates']
#    print ("# got this from json file: ", a)
    while i < len(a):        
        print ("\n#Polygon has #points: ", len(a[i]) ) 
        while j < len(a[i])-1:
            print ("\n***0 point", a[i][j][0])
            lon = a[i][j][0]*math.pi/180.0
            lat = a[i][j][1]*math.pi/180.0
            if (scheme == 0):
                if(vcount==0):
                    print("# Using cartesian system", file=jou)
                X, Y, Z = cartesian(lon,lat,0)
            else:
                if(vcount==0):
                    print("# Using UTM")
#                print (a[i][j][1], a[i][j][0])
                X, Y, zone, tnum  = utm.from_latlon(a[i][j][1], a[i][j][0])
                print ("create vertex ", X, Y, 0)
                print ("create vertex ", X, Y, 0, file=jou)

            vcount+=1
            if(xmin < abs(X)):
                xmin = X
            if(ymin < abs(Y)):
                ymin = Y
            if(xmax > X):
                xmax = X
            if(ymax > Y):
                ymax = Y
            j+=1
        c1 = vcount - len(a[i]) + 2
        c2 = vcount 
        print("create surf vertex ", c1, " to ", c2)
        print("create surf vertex ", c1, " to ", c2, file=jou)

        if (i == 0):
            scount+=1
        else:
            msurf_list.append(scount)
            print(" #Warning: Careful, we have two surface describing this building", file=jou)
        i+=1
        j=0
    
        
for m in range(len(msurf_list)):
    print("subtract body ", msurf_list[m] + 1, " from body ", msurf_list[m], file=jou)
    
tbodies = 0
numbodies = scount + len(msurf_list)
for i in range(numbodies):
    if (zmax < height[tbodies]):
        zmax = height[tbodies]
    found = 0
    extrudeheight = -height[tbodies]
    if (extrudeheight == 0):
        extrudeheight = 30
    if(len(msurf_list) != 0):
        for m in range(len(msurf_list)):
            if( i == msurf_list[m]):
                # do nothing since we this was a surface only meant for subtraction
#                print("thicken body ", scount+m, " depth ", -height[tbodies], file=jou)
                found = 1
        if (found == 0):
            print("thicken body ", i+1, " depth ", extrudeheight, file=jou)
            tbodies+=1

    else:
        print("thicken body ", i+1, " depth ", extrudeheight)
        print("thicken body ", i+1, " depth ", extrudeheight, file=jou)
        tbodies+=1

        

    
print("# min max", xmin, xmax, ymin, ymax, file=jou)
T = 1.2
TZ = 1.5
##
#print("create surface rectangle width ", abs(T*(xmax-xmin)), " height ", abs(T*(ymax-ymin))) 
#print("thicken body ", numbodies+1, " depth ", TZ*zmax)
#print("move vol ", numbodies+1, " x ", xmin + (xmax-xmin)/2.0, " y ", ymin + (ymax-ymin)/2.0, " x ", zmax/2.0)
#print("subtract vol  1 to ", numbodies, " from vol ", numbodies+1)

print("create surface rectangle width ", abs(T*(xmax-xmin)), " height ", abs(T*(ymax-ymin)), file=jou) 
print("thicken body ", numbodies+1, " depth ", TZ*zmax, file=jou)
print("move vol ", numbodies+1, " x ", xmin + (xmax-xmin)/2.0, " y ", ymin + (ymax-ymin)/2.0, " x ", zmax/2.0, file=jou)
print("vol 1 to ", numbodies, " copy", file = jou)
print("unite vol 1 to ", numbodies, file = jou)

print("subtract vol ", numbodies+2, " to ", scount+numbodies+1, " from vol ", numbodies+1, file=jou)

print("block 1 vol 1 to ", numbodies, file = jou)
print("block 2 vol ", numbodies+1, file = jou)

print("surf with z_coord = 0 size 3.0", file = jou)
print("imprint vol all\nmerge vol all\nmesh vol all\n", file=jou)
print("group 'g1' equals surf with area < 15000\ngroup 'g2' equals surf with z_coord = 0\ngroup 'g3' subtract g2 from g1", file = jou)
print("sideset 111 surf in g3", file = jou)
print("save as '" +  sys.argv[1]+ ".cub' over\nexit", file = jou)
##
jou.close()
bld.close()






