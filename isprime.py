# -*- coding: utf-8 -*-
"""
Created on Wed Aug 06 19:25:29 2014

@author: Kyle
"""

def isprime(n):
    lst=[]
    k=1
    for i in range(2,sqrt(n)):
        lst.append(i)
    for j in lst:
        if n%j==0:
            return False 
        else:
            while J*k<=sqrt(n):
                print lst
                lst.remove(j*k)
                k=k+1
                
            
    return True