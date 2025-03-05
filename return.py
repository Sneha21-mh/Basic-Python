#using return function
def fun(name ,location):
    return f'{name} ,{location}'
pr=fun('Sneha','Bangalore')
print(pr)

#use return
num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
def sum(num1,num2):
    return f'sum of {num1} and {num2} is {num1+num2}'
pr2=sum(num1,num2)
print(pr2)

#use return
s=input('enter a string:')
def st(s):
    return s[::-1]
pr3=st(s)
print(pr3)

