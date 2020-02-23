# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:28:16 2020

@author: adjimagnan

"""

class Prime:
    
def __init__(self, number):
    self.number=numer
    

def is_prime_number(n):
    count=1
    isprime=False
    
    for i in range(n):
        if i==0: 
            isprime=False
        else:
            if i=1 or i=2:
                isprime=False
            else:            
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
            p_list.append(k)
    print("Prime numbers in the range(", low,",", high, ")")
    return p_list 

generator=prime_number(30, 200)
print(generator)



def average(alist):
    count=0
    summe=0
    
    for n in alist:
        count+=1
        summe+=n
        print("sent:", n, ", new average:", round(summe/count, 2))
        
        
        
        
        
        
        