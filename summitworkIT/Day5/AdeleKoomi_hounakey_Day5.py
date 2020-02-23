# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:02:12 2020

@author: adjimagnan
"""
#==============================================================================
# Exception Assignment
# 1. Create a user defind exception class called nonintresultexception 
# which is generated when the result
# of dividing two integers values produces a result with a fractional 
# component[ i.e the result is not an integer]
# nonintresultexception contains:
# Generates an appropriate message , for example if the two integers 
# are 7 and 2 . The resulting 
# exception message would be 7 divided by 2 is not an integer
# 
#==============================================================================

class nonintresultexception(Exception):
    pass

try: 
   
   n1=int(input("Enter first integer : "))
   n2=int(input("Enter second integer : "))
   q=n2%n1 if n2>n1 else n1%n2
   if q==0:
        #a = 18-age;
        #print(a)
        raise nonintresultexception("Not an integer")
        
except nonintresultexception as t:
            print("the 2 integers are not divisible")
            print(t)
except ZeroDivisionError:
    print("Please enter two integers different to zero or if one is zero the other must be negative value")
              
except ValueError:
    print("please enter integers values...")
else:
    print("you entered proper values, thanks for the inputs")
    # load other services
    # load the services, depending on the location
finally:
    print("Goodbye
    ")


print("end of the app")
