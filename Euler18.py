__author__ = 'Kyle'

import numpy


n=100;
factorial=1
for i in range (1,n+1):
    factorial=i*factorial;

print factorial
y=factorial
count = 0
while y > 1:
    count += 1
    y = y/10
z=[0]*count
sum=0
x=factorial
for i in range(0,count):
    z[count-1-i]=(x)%(10)
    x=x-z[count-1-i]
    x=x/10

print len(z)
for i in range(0,len(z)):
    sum=sum+z[i]

print sum