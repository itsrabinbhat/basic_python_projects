#Inhertance
#inherits, extends, and override

#Parent class
class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def work(self):
        print("I am an Employee.")

#Child classes
class SoftwareEngineer(Employee):
    #Extending and overriding
    def __init__(self,name,age,salary,role):
        super().__init__(name,age,salary)
        self.role = role
    
    #extending
    def info(self):
        print(f"I'm {self.name} and I'm {self.age} yrs old.")

    #overriding
    def work(self):
        print(f"I am {self.role}")

class Manager(Employee):
    pass


se1 = SoftwareEngineer('John',24,5000,"Software Engineer")
print(se1.name)
se1.info()
se1.work()

m1 = Manager('Dan',34,7500)
print(m1.name)
m1.work()
