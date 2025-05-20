#dictionary methods
#1. create an empty dictionary
#2. ask user to enter name, email, mobile, city and pin from keyboard
#3. insert above pairs into dictionary.
#4. print all pairs of dictionary using for loop
#5. ask user to enter a different name and replace existing name with new name in the dictionary
#6. ask user to enter a key and if that key is available in the dictionary remove that pair
#7. ask user to enter a value and check if that value exists in the dictionary
#8. ask user to enter state, and insert that pair into dictionary.

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