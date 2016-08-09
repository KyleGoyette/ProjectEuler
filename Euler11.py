__author__ = 'Kyle'
#15
import math
#n=3;
#m=1;

#x=math.factorial(n+m)
#y=x/(math.factorial(n)*math.factorial(m))

#print x
#print y

#16
n=2;
m=1000;
x=math.pow(n,m);
y=x
count = 0
while y > 1:
    count += 1
    y = y/10
z=[0]*count
sum=0

for i in range(0,count):
    z[count-1-i]=(x)%(10)
    x=x-z[count-1-i]
    x=x/10

print len(z)
for i in range(0,len(z)):
    sum=sum+z[i]

print sum


