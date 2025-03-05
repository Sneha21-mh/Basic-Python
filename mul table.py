#multiplication table
x=int(input('enter the number:'))
num=x
while x<=(num*10):
    print(num,'*',x//num,'=',x)
    x=x+num
print('')