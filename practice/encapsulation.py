# Encapsulation
# Way of hiding data implementation(instance variables and methods are kept private)
# Use _ for Protected vars/methods
# Use __ for Private vars/methods

class Employee():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._salary = None
    
    #getter
    def get_salary(self):
        return self._salary
    
    #setter
    def set_salary(self,salary,work_hrs):
        self._salary = self._calc_salary(salary,work_hrs)
   
    #private method
    def _calc_salary(self,salary,work_hrs):
        if work_hrs <=40:
            return salary
        else:
            salary = int(salary + 0.1 * salary)
            return salary

    

se1 = Employee("Dan",34)
se2 = Employee("John",28)
print(se1.name, se1.age)
print(se2.name, se2.age)

# This represents abstraction
# You dont have access to the internal working of set_salary()
se1.set_salary(5000,36)
se2.set_salary(5000,45)

print(se1.get_salary())
print(se2.get_salary())