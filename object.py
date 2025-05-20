#take a student class with 2 methods.
# a)init method should take 3 parameters no , name , sub. init method should print no , name , sub
# b)display method should take 3 parameters no , name , sub.
# display method should print no , name , sub
# note: you have to call above 2 methods
class Student:
    def __init__(self,no,name,sub):
        print('No.:',no)
        print('Name:',name)
        print('Subject:',sub)
    def display(self,no,name,sub):
        print('No.:',no)
        print('Name:',name)
        print('Subject:',sub)
s=Student(1,'Sneha','English')
s.display(2,'Nandini','kannada')


#Initialize in init method ,display it in display method
class Student:
    def __init__(self,no,name,sub):
        self.no=no
        self.name=name
        self.sub=sub
    def display(self):
        print( 'No:',self.no)
        print('Name:',self.name)
        print('Subject:',self.sub)
s=Student(1,'Sneha','English')
s.display()



#create a student class with init and display methods.
# init method should have 3 parameters no,name,sub to initialize student object with values.
# display method should display student details.
# now create 3 student objects with below values.
# also display each student details with corresponding object
class Student:
    def __init__(self,no,name,sub):
        self.no=no
        self.name=name
        self.sub=sub
    def display(self):
        print( 'No:',self.no)
        print('Name:',self.name)
        print('Subject:',self.sub)
s=Student(1,'Sneha','English')
s.display()
t=Student(2,'Eshu','Kannada')
t.display()
r=Student(3,'Shanta','Hindi')
r.display()


#What is output for this code
class Patient:
    def __init__(self,name,disease,age):
        print('this is patient object')
        print('patient name=',name)
        print('disease=',disease)
        print('patient age=',age)
    def admitToRoom(self,roomno):
        print('patient is admitted in room',roomno)
p1=Patient('raj','viral fever',30)
p1.admitToRoom(101)


#calling z and y inside a function and outside the function
z=40
class Info:
    y=10
    x=30
    def m1(self):
        self.y=20
        print(self.y)
        print(i.x)
        print(z)
i=Info()
print(i.y)
i.m1()