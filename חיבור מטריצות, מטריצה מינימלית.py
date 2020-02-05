# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:45:39 2020

@author: שיר גבריאל
"""
def ret():
    a=[[1,2],[3,4],[1,2],[7,3]]
    b=[[1,2,3],[4,5,6]]
    c=[]
    d=[]
    if (len(a)>=len(b)):
        minx= len(b)
    else:
        minx=len(a)
    if (len(a[0])>=len(b[0])):
        miny= len(b[0])
    else:
        miny=len(a[0])
    for i in range (minx):
        for j in range (miny):
            summ = a[i][j] + b[i][j]
            d.append(summ)
        c.append(d)
        d=[]
    return (c)