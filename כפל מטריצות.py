# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:18:47 2020

@author: שיר גבריאל
"""
def ret():
    a=[[1,2],[3,4],[1,2],[7,3]]
    b=[[1,2,3],[4,5,6]]
    c=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for x in range (len(a)):
        for i in range (len(b[0])):
            for z in range (len(b)):
                c[x][i] = c[x][i] + a[x][z]*b[z][i]
    
    return(c)