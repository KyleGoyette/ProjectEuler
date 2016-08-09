# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 21:00:46 2014

@author: Kyle
"""

orig=4 #600851475143
i=2

while i*i<=orig:
    
        while orig%i==0:
            orig=orig/i
        i=i+1
        

print orig