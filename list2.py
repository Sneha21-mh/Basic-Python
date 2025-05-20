#list methods
#append method
li=[20]
li.append(10)
print(li)

#pop method
li=[10,20,30,40,50]
li.pop(2)
print(li)

#remove method
li=[10,20,30,50,40,50]
li.remove(50)
print(li)

#extend method
li=[10,20,30,40,50]
li.extend([50,70,80])
print(li)

#reverse method
li=[10,20,30,40,50]
li.reverse()
print(li)

#insert method
li=[10,20,30,40,50]
li.insert(3,100)
print(li)

#use append method
# 1. take an empty list
# 2. read and store 10 elements from keyboard and store in list
# 3. print all list elements
# 4. ask user to enter a position and element from the keyboard, and insert that element before that position
# 5. ask user to enter an element to delete from the list, and delete that element if it is available
# 6. ask user to enter a position, and delete that element from the list if that position is available
# 7. ask user to enter an element and print the position of that element if available, else print-1

li = []
print('enter the elements:')
for i in range(10):
    num = int(input())
    li.append(num)
print(li)

#use insert method
pos=int(input('enter the position to be added:'))
new=int(input('enter the new element to be added:'))
li.insert(pos,new)
print(li)

#use remove method
delete=int(input('enter the element to delete:'))
if delete in li:
    li.remove(delete)
    print(li)
else:
    print('It is not present in the list')

#use pop method
dlt=int(input('enter the index from which element has to be deleted:'))
if dlt in range(len(li)):
    li.pop(dlt)
    print(li)
else:
    print('Index is not available')

#use index method
elem=int(input('enter the element whose index to be found:'))
if elem in li:
    position=li.index(elem)
    print(position)
else:
    print('-1')

#use index method
li=[2,3,4,5,6,7]
elem = int(input('enter the element whose index to be found:'))
if elem in li:
    print(li.index(elem))
else:
    print(-1)
