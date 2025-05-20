#area of triangle

height=float(input('Enter the height of triangle:'))
base=float(input('Enter the base of triangle:'))
area=1.5*base*height
print('area of triangle is',area)


#miles to kilometers

miles=float(input('enter the miles:'))
km=miles*1.6
print(miles,'miles=',km,'km')


#swapping

num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
print('before swapping',num1  , num2)
num3=num1
num1=num2
num2=num3
print('after swapping',num1,num2)


#celcius to fahrenheit

celc=float(input('enter the celcius:'))
faren=(celc*9/5)+32
print(celc,'celcius=',faren,'fahrenheit')


#position or negative

num=int(input('enter the number:'))
if num>0:
    print(num,'is positive')
elif num<0:
    print(num,'is negative')
else:
    print(num,'is zero')


#multiplication table

x=int(input('enter the number:'))
num=x
while x<=(num*10):
    print(num,'*',x//num,'=',x)
    x=x+num
print('')


#sum within an interval

num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print('The sum between',num1,'and',num2,'is',sum)
