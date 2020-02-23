'''
Created on Jul 26, 2017

@author: SummitWorks
'''

class Driver:
    def __init__(self,name):
        self.name=name
    def test(self):
        print(self.name)
class Car:
    def __init__(self,cname):
        self.cname=cname
    def testc(self):
        print(self.cname)
    def getDriverDetails(self,d):
        d.test()
        d1=Driver("ram")
        d1.test()
d=Driver("Raj")
d.test()
c=Car("santro")
c.testc()
c.getDriverDetails(d)

        

