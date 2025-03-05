#dictionary with loops
di={
    'x':10,
    'y':20
}
for i in di:
    print(i,di[i])


#displaying items
di={
    'x':10,
    'y':20
}
for i,j in di.items():
    print(i,j)


#displaying keys
di={
    'x':10,
    'y':20
}
for i in di.keys():
    print(i)


#displaying values
di={
    'x':10,
    'y':20
}
for i in di.values():
    print(i)


#displaying both keys and values
di={
    'x':10,
    'y':20
}
for i,j in di.items():
    print(i,'=',j)


#take input from keyboard
house_no=int(input('enter the house number:'))
street=input('enter the street:')
city=input('enter the city:')
pin=int(input('enter the pincode:'))

di={
    'house number':house_no,
    'street':street,
    'city':city,
    'pincode':pin
}
for i,j in di.items():
    print(i,'=',j)


#append
li=[]
for i in range(5):
    num=int(input('enter the number:'))
    li.append(num)
print(li)


#palindrome
num=int(input('enter the value:'))
res=num
rev=0
while num>0:
    res=num%10
    rev=(rev*10)+res
    num=num//10
if rev==res:
    print(res,'is a palindrome')
else:
    print(res,'is not a palindrome')