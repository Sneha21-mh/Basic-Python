
class Details:
    x=10
    def m1(self):
        print('hello')
d=Details()
print(d.x)
d.m1()



#
name=input('enter the name:')
age=int(input('enter the age:'))
location=input('enter the location:')
class PersonalDetails:
    def display_details(self,name,age,location):
        print(name,age,location)
p=PersonalDetails()
p.display_details(name,age,location)



#Create a class named MathOperations.it should contain 4 methods to find out sum,difference,product and quotient.
#Each method takes two parameters .Create an object for the class and call each method .Take input from keyboard.
x=int(input('enter the first number:'))
y=int(input('enter the second number:'))
class MathOperations:
    def sum(self,x,y):
        print('The sum of',x,'and',y,'is',x+y)
    def diff(self,x,y):
        print('The difference between',x,'and',y,'is',x-y)
    def product(self,x,y):
        print('The product of',x,'and',y,'is',x*y)
    def quotient(self,x,y):
        print('The quotient when',x,'is divided from',y,'is',x//y)
m=MathOperations()
m.sum(x,y)
m.diff(x,y)
m.product(x,y)
m.quotient(x,y)



z=30
class A:
    y=20
    def m1(self):
        x=10
        print(x)
        print(A.y)
print(z)
print(A.y)
a=A()
a.m1()



#assume that your writing a python application for a training institute.
#come up with at least 4 classes where each class will have 2 methods
class ProfessionalDetails:
    def college(self):
        print('I studied in STJIT college')
    def course(self):
        print('I want to do python fullstack course')

class PersonalDetails:
    def address(self):
        print('I am from Ranebennur')
    def mobile_number(self):
        print('My mobile number is ',9876543210)

pr=ProfessionalDetails()
pr.course()
pr.college()
p=PersonalDetails()
p.address()
p.mobile_number()



#__init__ (Constructor)
class Python:
    def __init__(self):
        print('Hello')
p=Python()



#Create a class named Info with a constructor that takes 3 parameters id,name,course and print them .
#Create 3 separate instances of that class
class Info:
    def __init__(self,id,name,course):
        print('ID:',id)
        print('Name:',name)
        print('Course:',course)
a=Info(1,'Sneha','Python')
b=Info(2,'Eshu','Java')
c=Info(3,'Shashi','C++')


#Call the arguments in another method using self variable
class Info:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course
    def m1(self):
        print(self.id)
        print(self.name)
        print(self.course)
a=Info(1,'Sneha','Python')
a.m1()
b=Info(2,'Eshu','Java')
b.m1()
c=Info(3,'Shashi','C++')
c.m1()



#Create a class named MathOperation with a constructor that takes 2 numbers as parameters . Create separate methods for
# addition , subtraction,multiplication,division which print the results.Call those methods
class MathOperation:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addition(self):
        print(self.x+self.y)
    def subtraction(self):
        print(self.x-self.y)
    def multiplication(self):
        print(self.x*self.y)
    def division(self):
        print(self.x//self.y)
m=MathOperation(25,5)
m.addition()
m.subtraction()
m.multiplication()
m.division()