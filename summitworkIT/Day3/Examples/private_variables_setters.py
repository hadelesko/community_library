'''
Created on Jun 22, 2017

@author: SummitWorks
'''
class Car:
    __maxspeed = 0
    __name = ""
    _test=""
    count=0
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
        Car.count+=1
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
    def getMaxSpeed(self):
        return self.__maxspeed
redcar = Car()
redcar.drive()
redcar.__maxspeed=600
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
print(redcar.getMaxSpeed())
print(redcar.__maxspeed)

