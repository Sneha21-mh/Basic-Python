#pallindrome or not
a=input('enter the string:').lower()
if a==a[::-1]:
    print('pallindrome')
else:
    print('not a pallindrome')