# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:49:28 2020

@author: שיר גבריאל
"""
import numpy as np
def ret():
    a=[[1,2],[3,4],[1,2],[7,3]]
    b=[[1,2,3],[4,5,6]]
    c=[]
    if (len(a)<=len(b)):
        maxx= len(b)
    else:
        maxx=len(a)
    if (len(a[0])<=len(b[0])):
        maxy= len(b[0])
    else:
        maxy=len(a[0])
    c= np.zeros((maxx,maxy))
    for x in range (len(a)):
        for y in range(len(a[0])):
            c[x][y]+= a[x][y]
    for x in range (len(b)):
        for y in range(len(b[0])):
            c[x][y]+= b[x][y]       
