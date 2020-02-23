'''
Created on Jul 1, 2017

@author: SummitWorks
'''
# steps:
# create a class with exception name , chaild class of Exception
# use raise keyword whenever you raise the exception manully as Python Interpreter deont know

class TooYoungException(Exception):
    pass

try:
    age=int(input("Enter age of the customer"))
    if age<18:
        #a = 18-age;
        #print(a)
        raise TooYoungException("less than 18 years , not eligible to vote now")
        
except TooYoungException as t:
            print("you are not eligible to vote now")
            print(t)
except ValueError:
    print("please enter valid age...")
else:
    print("you are eligible to vote, thanks for vote")
    # load other services
    # load the services, depending on the location
finally:
    print("its a finally block")


print("end of the app")
    
    
