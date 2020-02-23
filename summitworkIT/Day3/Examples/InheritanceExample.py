'''
Created on Jun 22, 2017

@author: SummitWorks
'''
class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")
        
#     def whoAmI(self,a):
#         print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

#We put the ancestor classes in round brackets after the name of the descendant class. 
#If the derived class provides its own __init__() method, it must explicitly call the base class __init__() method.

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    # overriding
    def whoAmI(self):
        Animal.eat(self);
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()
a=Animal()
a.whoAmI()