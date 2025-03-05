#use for loop in list
li=[10,20,13,61,50]
print('elements at even indices are:')
for i in range(0,5,2):
    print(li[i],end=' ')
print(' ')
print('elements at odd indices are:')
for i in range(1,5,2):
    print(li[i],end=' ')
print(' ')

#even or odd
li=[10,20,13,61,50]
for i in range(0,5,1):
    if li[i]%2==0:
        print(li[i], 'is a even element')
    else:
        print(li[i], 'is a odd element')

#sum
li=[10,20,13,61,50]
sum = 0
for i in li:
    sum=sum+i
print('the sum is',sum)

#sum of even and odd elements
li=[10,20,13,61,50]
sum_even=0
sum_odd=0
for i in range(0,5,1):
    if li[i]%2==0:
        sum_even=sum_even+li[i]
    else:
        sum_odd=sum_odd+li[i]
print('sum of even elements',sum_even)
print('sum of odd elements',sum_odd)

#sum of elements at even and odd indices
li=[10,20,13,61,50]
print('sum of the elements at even indices is:')
sum_even=0
for i in range(0,5,2):
    sum_even=sum_even+li[i]
print(sum_even)
print(' ')
print('sum of the elements at odd indices is:')
sum_odd=0
for i in range(1,5,2):
    sum_odd=sum_odd+li[i]
print(sum_odd)
print(' ')