'''
Created on Aug 4, 2017

@author: SummitWorks
'''
class Human:
 
    def sayHello(self, name="Maruthi"):
 
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
            
    #def sayHello(self,name,did1,phone):
        #print("hello")
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
 
# Call the method with a parameter
obj.sayHello('Guido')
print(obj)