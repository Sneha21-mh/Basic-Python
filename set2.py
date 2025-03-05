#set method
#add method
st=set()
print('Enter the numbers:')
for i in range(5):
    elem=int(input())
    st.add(elem)
print(st)

#remove method
dlt=int(input('enter the element to be deleted:'))
if dlt in st:
    st.remove(dlt)
    print(st)
else:
    print(dlt,'is not present in set')