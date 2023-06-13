# Pythonic way of using getter and setter methods

class Employee():
    def __init__(self):
        self._salary = None

    #getter
    @property
    def salary(self):
        return self._salary
    
    #setter
    @salary.setter
    def salary(self,salary):
        self._salary = salary[0]
        print(salary[1])
    #deleter
    @salary.deleter
    def salary(self):
        del self._salary

    
emp1 = Employee()
emp1.salary = (6000,40)
print(emp1.salary)