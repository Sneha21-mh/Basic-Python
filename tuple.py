tu=(10,20,30,40,50)
print(tu)
li=list(tu)
print(li)

#tuple methods
# 1. take an empty tuple
# 2. insert 5elements from keyboard
# 3. ask user to enter an element from keyboard,and delete that element from tuple
# 4. ask user to enter an element from keyboard and print the position of that element

tu=(10,20,30,40,50,10)
print(tu)
elem=int(input('enter the element whose index has to be determined:'))
if elem in tu:
    print(tu.index(elem))
else:
    print(elem,'is not present in tuple')

#index method
tu=(10,20,30,40,50)
elem=int(input('enter the element whose index has to be determined:'))
if elem in tu:
    pos=tu.index(elem)
    print(pos)
else:
    print(elem,'is not present in tuple')
