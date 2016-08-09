# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Kyle\.spyder2\.temp.py
"""
pali=False
for i in range(900,999):
    pali=False
    for j in range(900,999):
        pali=False
        num=i*j
        check=map(int,str(num))
        var=len(check)
        for k in range(len(check)):
            if check[k]==check[len(check)-k-1]:
                pali=True
            else:
                pali=False
                break
        if pali==True:
            
            palindrome=num
            itot=i
            jtot=j
    
print palindrome
print itot
print jtot
        
