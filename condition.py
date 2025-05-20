#biggest value among 2 numbers
num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))

if num1>num2:
    print(num1 ,'is bigger than ', num2)
else:
    print(num2 ,'is bigger than ',num1)


#even or odd
a=int(input('enter th number:'))
if a%2==0:
    print(a,'is even number')
else:
    print(a,'is odd number')



#biggest value among 3 numbers
x=int(input('enter the first number:'))
y=int(input('enter the second number:'))
z=int(input('enter the third number:'))
if (x>y) and (x>z):
    print(x,'is biggest among',y ,'and', z)
elif y>z:
    print(y,'is biggest among',x,'and',z)
else:
    print(z,'is biggest among',x,'and',y)