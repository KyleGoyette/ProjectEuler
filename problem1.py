# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 20:18:56 2014

@author: Kyle
"""
fib=1
fib_new=1
sum_fib=0
while fib_new<4000000:
    if fib_new %2==0:   
        sum_fib=sum_fib+fib_new
        
    print fib_new
    if fib_new==1:
        fib_new=2
    else:
        temp=fib_new+fib
        fib=fib_new
        fib_new=temp

print sum_fib