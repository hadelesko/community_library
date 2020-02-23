# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 07:52:30 2020

@author: adjimagnan
"""

def largest_number(numberlist):## max(numberlist)---> max(numberlist)
    maxnumber=numberlist[0] # initialize the max as the first element in the list
    for n in numberlist:
        maxnumber=maxnumber if maxnumber>=n else n 
    return maxnumber
def max_counter(numberlist):
    occurrence=0
    for number in numberlist:
        occurrence+=1 if number==largest_number(numberlist) else occurrence
    return occurrence

def max_and_occurrence():
    numbers= input("Enter the numbers: ")
    if int(numbers[-1])==0:
        numberlist=[int(i) for i in numbers[:-1]]
        print("The largest number is", largest_number(numberlist))
        print("The occurrence count of the largest number is", max_counter(numberlist))
        print(numbers)
#    else:
#        print("Try again")