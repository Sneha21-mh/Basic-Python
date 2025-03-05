#using different parameters
def patient(p_name,blood_g,*dis,e_mail='not given'):
    print('patient name=',p_name)
    print('Blood group=',blood_g)
    for i in dis:
        print(i,end=',')
    print('')
    print('E_mail=',e_mail)
patient('peter','B+','cancer','cold','low BP',e_mail='peter@gmail.com')
print('')
patient('bob','O-','high BP','blood cancer',e_mail='bob@gmail.com')
print('')
patient('Pinki','AB+','cancer')
print('')

#use different parameters
def student(s_name,*e_mail,**address):
    print('Student name=',s_name)
    for i in e_mail:
        print(i,end=',')
    print('')
    for i,j in address.items():
        print(i,'=',j)

student('sneha','sneha@gmail.com','sahana@gmail.com',city='Mangalore',house_no=1234)
print('')
student('sahana','sahana@gmail.com',city='Bangalore',state='karnataka')