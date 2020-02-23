'''
Created on Aug 2, 2017

@author: SummitWorks
'''
class Cup:
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None
class Test(Cup):
    def test_me(self,con):
        print(self._content)
        self._content=con
        print(self._content)
cup = Cup()
cup._content = "tea"
t=Test()
t.test_me("red")