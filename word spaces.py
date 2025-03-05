#words and spaces
x=input('enter the string:')
word=1
space=0
for i in x:
    if i==' ':
        space=space+1
        word=word+1
print('number of words:',word)
print('number of spaces:',space)

#vowel or not
vowels=['a','e','i','o','u']
words=input('enter a list of words:')
char=input('enter the character:')
for i in vowels:
    print(char ,'is a vowel')
    break;
print(char,'is not a vowel')

#biggest and smallest
li=[100,250,30,450,5]
largest=0
for i in li:
    if i>largest:
        largest=i
print(largest,'is biggest')


li=[100,250,30,450,5]
smallest=450
for i in li:
    if i<smallest:
        smallest=i
print(smallest,'is smallest')