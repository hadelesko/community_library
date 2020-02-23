# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 05:48:41 2020

@author: adjimagnan
"""

##Day3

#==============================================================================
# Generators
#  Create a generator that yields "n" random numbers
#  between a low and high number (that are inputs).
#  Note: Use the random library. 
#==============================================================================
#==============================================================================
# Iterators generator
# Display prime numbers from n1 to n2 using iterators and generators.
# 30 to 200: iterator protocal
# Generator method to get prime numbers from 30 to 200.
# 
# write two python programs using both iterators and generators.
#==============================================================================
#==============================================================================
# Inheritance Poly
# Inheritahce and Polymorphism
# (The Person, Student, Employee, Faculty, and Staff classes) Design a
# class named Person and its two subclasses named Student and Employee.
# Make Faculty and Staff subclasses of Employee. A person has a name,
# address, phone number, and email address. A student has a class status (freshman,
# sophomore, junior, or senior). Define the status as a constant. An employee has an
# office, salary, and date hired.A faculty member has office hours
# and a rank. A staff member has a title. Override the repr() function in each
# class to display the class name and the persons name.
#  Write a test code that creates a Person, Student, Employee, Faculty, and Staff.
#==============================================================================


import random as r
def randomrange(n,m):
    low = n  if n < m else m
    high= m  if n<m else n
    for i in range(low,high):
        yield r.randint(i, high)
f= randomrange(50, 45)
for x in f:
    print(x)
    
class prime:
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2
    
    def __iter__(self):
        return self
    
    def next(self):
        low = n  if n < m else m
        high= m  if n<m else n
        if low>1:
            for i in range(2, low):
                if(low % i==0):
                    continue
                yield low
        
def prime_iter_generator(n1, n2):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    