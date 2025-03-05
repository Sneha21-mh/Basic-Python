#dictionary methods
d={}
name=input('Enter your name:')
e_mail=input('Enter your e mail:')
city=input('Enter the city:')
mobile=int(input('enter your mobile number:'))
pin=int(input('Enter the pincode:'))
print(' ')

d['Name']=name
d['E_mail']=e_mail
d['City']=city
d['Mobile no.']=mobile
d['Pincode']=pin

for i,j in d.items():
    print(i,'=',j)
print('')

new=input('Enter a new name :')
d['Name']=new
print('Your updated information is')
for i,j in d.items():
    print(i,'=',j)
print('')

key=input('Enter the key to be deleted:')
if key in d.keys():
    (d.pop(key))
    for i, j in d.items():
        print(i, '=', j)
else:
    print('The key is not present in dictionary')
print('')

value=input('Enter the value to be checked:')
if value in d.values():
    print('The value is present in the dictionary')
else:
    print('The value is not present in the dictionary')
print('')

state=input('enter the state:')
d['state']=state
print('Your updated information is')
for i, j in d.items():
    print(i, '=', j)