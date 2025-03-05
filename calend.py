#calendar
import calendar
year=int(input('enter the year:'))
month=int(input('enter the month:'))
display=calendar.month(year,month)
print(display)

#datetime
import datetime
print(datetime.datetime.now())

#math
import math
print(math.factorial(5))

#factorial
num=int(input('enter the number:'))
fact=num
for i in range(1,num):
    fact=fact*i
print('factorial of',num,'is',fact)