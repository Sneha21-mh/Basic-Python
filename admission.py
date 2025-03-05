name=input('enter your name:')
gender=input("enter your gender: ").lower()
if gender=='male':
    height = int(input('enter the height:'))
    if height>=188:
        print(name,',you are eligible for admission')
    else:
        print(name,',you are not eligible for admission')
elif gender=='female':
    height = int(input('enter the height:'))
    if height>=175:
        print(name,',you are eligible for admission')
    else:
        print(name,',you are not eligible for admission')
else:
    print('Please enter your gender correctly')
