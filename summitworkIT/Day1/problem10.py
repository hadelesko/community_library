# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:38:17 2020

@author: adjimagnan
"""

# Problem 10
def numberseries():
#(n_row, max_column):
    a=" 1 2 3 4 5 6 7 "
    # using the built -in function len()

    for i in range(6):
        # spaceBeforeAfter=" "*i
    
        print(" "*i + a[2*i+1:] + ""*i)
    
    for j in range(7):
        #print(""*(7-i)+a[-2-2*j:]+""*i)
        m=6-j  # Spaces before and after numbers or indentation 
        print(" "*m+a[-2-2*j:]+""*j)
        
# Problem 9
def displaystarseries():
       
   starslist= " * * * * * "
   for j in range(len(a)//2+1):
       n=len(starslist)//2-j  # Spaces before and after numbers or indentation
       print(" "*n+starslist[-1-2*j:]+""*j)     