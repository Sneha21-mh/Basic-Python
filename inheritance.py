'''
#Example for Single level inheritance
class A:
    def m1(self):
        print('Class A function')
class B(A):
    def m2(self):
        print('Class B function')
b=B()
b.m1()
b.m2()
print('')

#Example for Multilevel inheritance
class A:
    def m1(self):
        print('Class A function')
class B(A):
    def m2(self):
        print('Class B function')
class C(B):
    def m3(self):
        print('Class C function')
c=C()
c.m1()
c.m2()
c.m3()
print('')

#Another example for Multilevel inheritance
class A:
    x=10
class B(A):
    y=20
class C(B):
    z=30
c=C()
print(c.x)
print(c.y)
print(c.z)
print('')

#hierarchical inheritance
class A:
    def m1(self):
        print('Class A function')
class B(A):
    def m2(self):
        print('Class B function')
class C(A):
    def m3(self):
        print('Class C function')
b=B()
b.m1()
b.m2()
c=C()
c.m1()
c.m3()
print('')

#Multiple inheritance
class A:
    def m1(self):
        print('Class A function')
class B:
    def m2(self):
        print('Class B function')
class C(A,B):
    def m3(self):
        print('Class C function')
c=C()
c.m1()
c.m2()
c.m3()
print('')

#Hybrid inheritance
class A:
    def m1(self):
        print('Class A function')
class B(A):
    def m2(self):
        print('Class B function')
class C(A):
    def m3(self):
        print('Class C function')
class D(B,C):
    def m4(self):
        print('Class D function')
d=D()
d.m1()
d.m2()
d.m3()
d.m4()
print('')

#Another example for hybrid/diamond inheritance
class A:
    x=10
class B(A):
    y=20
class C(A):
    z=30
class D(B,C):
    a=40
d=D()
print(d.x)
print(d.y)
print(d.z)
print(d.a)
'''


'''
#Implement a student grading system.
# Create a class student with following
#A constructor to initialize the student's name,roll no and marks in three subjects.
#A method calculate_average() to calculate the average marks.
#A method display_grade() display the grade based on the average marks
#A for avg>=90
#B for avg>=75 and <90
#C for avg>=50 and <75
#F for avg<=50
class Student:
    def __init__(self,name,roll,mark1,mark2,mark3):
        self.name=name
        self.roll=roll
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calculate_average(self):
        sum=self.mark1+self.mark2+self.mark3
        self.mark3=sum/3

    def display_grade(self):
        if self.mark3>=90:
            print('A')
        elif (self.mark3>=75) and (self.mark3<90):
            print('B')
        elif (self.mark3>=50) and (self.mark3<75):
            print('C')
        else :
            print('F')
s=Student('Sneha',20,95,95,100)
s.display_grade()

'''
#Implement a banking system
#Create a class BankAccount that simulates a simple Banking system.
#Implement the following:
#A constructor to initialize the account holder's name,account no and balance(default is 0).
#A method deposit(amount) to add money to the account
#A method withdraw(amount) to withdraw money , ensuring the balance does not go negative.
#A method display_balance() to display current balance
class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,d_amount):
        self.balance=self.balance+d_amount
        print('Deposited amount is',d_amount,'.Balance is',self.balance)
    def withdraw(self,w_amount):
        if w_amount>self.balance:
            print('Insufficient balance')
        else:
            self.balance=self.balance-w_amount
            print('Withdrawn',w_amount,'.Balance is',self.balance)
    def display_balance(self):
        print('Total Account Balance is',self.balance)
b=BankAccount('Sneha',1234,4000)
b.deposit(2000)
b.withdraw(1000)
b.display_balance()