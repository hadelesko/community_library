# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 04:59:35 2020

@author: adjimagnan
"""
def is_prime_number(n):
    count=1
    isprime=False
    
    if n==0: 
        isprime=False
    else:
        if n==1 or n==2:
            isprime=True
        else:
            for i in range(2, n):            
                if n%i==0:
                    count+=1
                    isprime=False
                    ##print("is not prime number")
                    break
                isprime=True
    return isprime

    #return isprime

    
def prime_number(n, m):
    p_list=[]
    low = n  if n < m else m
    high= m  if n<m else n
    for k in range(low, high):
        if is_prime_number(k)==True:
            yield k
            p_list.append(k)
    print("Prime numbers in the range(", low,",", high, ")")
    #return p_list 

generator=prime_number(30, 200)
print([s for s in generator]) 


#==============================================================================
#     Write a generator which computes the running average for any given list
#     e.g. input - [7, 13, 17, 231, 12, 8, 3]
#     output - sent: 7, new average: 7.00 sent: 13, new average: 10.00
#     sent: 17, new average: 12.33 sent: 231, new average: 67.00
#     sent: 12, new average: 56.00 sent: 8, new average: 48.00
#     sent: 3, new average: 41.57
#==============================================================================
def average(alist):
    count=0
    summe=0
    
    for n in alist:
        count+=1
        summe+=n
        yield "sent: "+ str(n)+ ", new average: "+str(round(summe/count, 2))
        
d=average([31, 37, 41, 43, 47, 53, 59, 61, 67])
for line in d:
    print(line)
    
    
    