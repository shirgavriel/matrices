# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:27:54 2020

@author: שיר גבריאל
"""
import numpy as np
import random

def cefel(a,filt):
    newa = np.random.rand(len(a)-2,len(a)-2)

    for row in range (len(a)-2): #לולאה גדולה של טורים       
        for line in range (len(a)-2):               
               for i in range (3):  #לולאה של כפל מטריצה 3X3 
                   for m in range (3):
                       newa[row][line]+=a[i][line+m]*filt[i][m]
     return newa
 
def main():
    a = []
    filt = []
    new = []
    filt = np.random.rand(3,3)
    for x in range (3):
        for y in range (3):
            filt[x][y] = filt[x][y]*random.choice([1,2,3,4,5])
    new = cefel(a,filt)
    print (new)
    while (len(new)>len(filt)):
        new = cefel(a,filt)
        print (new)

                
                
                
                
                
                
                
                
                
                