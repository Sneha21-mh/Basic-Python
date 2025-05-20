#Use try and except block
li=[10,20,30,40,50]
try:
    print(li[5])
except:
    print('error occurred')


#Exception as e
li=[10,20,30,40,50]
try:
    print(li[5])
except Exception as e:
    print(e)


#use multiple try and except block to find all the errors,otherwise it will show only one error which is appeared first
try:
    x = int(input('enter the number:'))
    print(x)
except Exception as e:
    print(e)
try:
    y = [10, 20, 30]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
except Exception as e:
    print(e)


#Named exceptions and generic exception
x=[10,20,30,40,50]
y=10
try:
    print(x[0])
    print(y/0)
except IndexError:          #Named exception
    print('Trying to access a non existent index')
except ZeroDivisionError:   #Named exception
    print('Trying to divide a number by 0')
except:                     #Generic exception
    print('An error occurred')

