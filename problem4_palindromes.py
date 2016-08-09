# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 22:42:17 2014

@author: Kyle
"""

#largest palindrome by product of 3 digit numbers
# largest multiple of 11 <1000
#
i=range(999)
elevs=i[99::11]
print elevs


for i in elevs:
    for j in range(100, 999):
        test=i*j
        
        print test
    
#    for j in range(, 999,11) if j%11==0:
        
#        filter(lambda x: x == i or x % i, nums)
#        test=(i*j)
#        test=str(test)
#        for c in test:
#            
#        print test
        #if test==909909:
         #  print test
          # print i 
           #print j
            
        
      #  if (i*j)