#Creating a class
class MyClass():
    #class attribute
    class_atr = "this is class attribute."
    #Defining init function
    def __init__(self,fname,lname):
        self.firstname = fname #self.sth instance attribute
        self.lastname = lname

    #Creating a method inside a class
    def full_name(self):
        return f'Welcome {self.firstname} {self.lastname}'

    def __str__(self):
        info = f'{self.firstname} is a good person.'
        return info

    #this d-under method determines the comparision of two instances
    def __eq__(self,other):
        return self.firstname == other.firstname
    
    #@staticmethod is used to define function without self parameter
    #these methods are not tied to any particular instances
    @staticmethod
    def base_salary(age):
        if age < 20:
            return 3000
        elif age < 25:
            return 5000
        else:
            return 8000

#creating an instance 
user1 = MyClass('Brim','Rawal')
user2 = MyClass('Brim','Rawal')
user3 = MyClass('Jack','Daniels')

#calling the method fullname()
print(user1.full_name())

#displaying class attribute
print(user1.class_atr)

#this compares memory address for user1 and user2 without __eq__ method
print(user1 == user2)

print(user1.base_salary(22))
