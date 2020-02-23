class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    @staticmethod
    def displayCount(): # static functions
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self): # instance functions
        print("Name : ", self.name, ", Salary: ", self.salary)
    

e1 = Employee("John",6500)
e2 = Employee("Raj",8500)
print(e1.name)
print(e2.name)
e1.name = "John_W"
print(Employee.empCount)
Employee.displayCount()
e1.displayEmployee()

Employee.displayCount()
e2.displayEmployee()

e1.displayCount()
e2.displayCount()
