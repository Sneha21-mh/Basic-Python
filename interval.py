#sum within an interval
num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print('The sum between',num1,'and',num2,'is',sum)