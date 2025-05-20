
a=int(input('enter the first value:'))
b=int(input('enter the second value:'))
def add(a,b):
    return f'The sum of {a} and {b} is {a+b}'
result=add(a,b)
print(result)

def mul(a,b):
    return f'The product of {a} and {b} is {a*b}'
result=mul(a,b)
print(result)

def div(a,b):
    return f'The division of {a} from {b} is {a/b}'
result=div(a,b)
print(result)

def sub(a,b):
    return f'The subtraction between {a} and {b} is {a-b}'
result=sub(a,b)
print(result)

def mod(a,b):
    return f'The remainder of {a} when it is divide from {b} is {a%b}'
result=mod(a,b)
print(result)
