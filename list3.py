
#displaying even numbers from 0 to 100
li=[]
for i in range(0,101,2):
    li.append(i)
print(li)


li=[1,5,6,8,3]
#display [25,64] for given list , in one line
y=[li[i]**2 for i in range(5) if i%2!=0]
print(y)

#display [5,30,15] for given list , in one line
y=[li[i]*5 for i in range(5) if i%2==0]
print(y)

#display [2,10,12,16,6] for given list , in one line
y=[li[i]*2 for i in range(5) ]
print(y)

#display [25,64] for given list
li=[1,5,6,8,3]
y=[]
for i in range(5):
    if i%2!=0:
        y.append(li[i]**2)
print(y)

#display [5,30,15] for given list
y=[]
for i in range(5):
    if i%2==0:
        y.append(li[i]*5)
print(y)

#display [2,10,12,16,6] for given list
y=[]
for i in range(5):
    y.append(li[i]*2)
print(y)



li=[11,3,6,10,13]
y=[]
for i in range(5):
    if li[i]%3==0:
        y.append(li[i]**2)
print(y)

y=[]
for i in range(5):
    y.append(li[i]+5)
print(y)

y=[]
for i in range(5):
    if li[i]%3!=0:
        y.append(li[i]**2)
print(y)


y=[li[i]**2 for i in range(5) if li[i]%3==0]
print(y)


y=[li[i]+5 for i in range(5) ]
print(y)

y=[li[i]**2 for i in range(5) if li[i]%3!=0]
print(y)
'''

'''
x=['hi','python','we','write','python','we','say','hi','python']
#output should be {'hi': 2, 'python': 3, 'we': 2, 'write': 1, 'say': 1}
di={}
for i in x:
    if i in di.keys():
        di[i]=di[i]+1
    else:
        di[i]=1
print(di)



x=[('a',10),('b',20),('c',30),('d',40)]
for i in x:
    print(i[1],end=' ')


x=['a','b','c','d']
y=[10,20,30,40]
di={}
for i in range(4):
    di[x[i]]=y[i]
print(di)

x=['a','b','c','d']
y=[10,20,30,40]
z=[]
print(z)