#tuple methods
#index method
tu=(10,20,30,40,50)
elem=int(input('enter the element whose index has to be determined:'))
if elem in tu:
    print(tu.index(elem))
else:
    print(elem,'It is not present in tuple')

#index method
tu=(10,20,30,40,50)
elem=int(input('enter the element whose index has to be determined:'))
if elem in tu:
    pos=tu.index(elem)
    print(pos)
else:
    print(elem,'It is not present in tuple')
