# -*- coding: utf-8 -*-
"""
Created on Sun Aug 03 19:02:25 2014

@author: Kyle
"""
i=1000000
div=False
while div==False:
    i=i+2
    div=False
    for j in range(1,20):
        if i%j==0:
            div=True
        else:
            div=False
            break
    if div==True:
        print i
        
print i

#232792560
