'''
f=open('sample.txt','w')
f.write('This is file operation')
f.close()


f=open('sample.txt','w')
f.write('this is the another file')
f.close()


f=open('sample.txt','a')
f.write('\nthis is new content')
f.close()


f=open('sample.txt','r')
res=f.read()
print(res)
print('')

f=open('sample.txt','r')
res=f.readline()
print(res)

f=open('sample.txt','r')
res=f.readlines()
print(res)

'''
from dataclasses import replace

#Create a file named info.txt .Open the file and write two lines.Close the file.Add two more lines to the file.
#Read the content of the files
'''
f=open('info.txt','w')
f.write('Good morning ')
f.write('\npython class')
f.close()
f=open('info.txt','a')
f.write('\nLet us begin the class ')
f.write('\nsee you')
f.close()

f=open('info.txt','r')
res=f.read()
content=res.replace('Good morning','we have made a changes')
f.close()
print(content)
f=open('info.txt','w')
f.write(content)
f.close()


'''

f=open('python.txt','w')
f.write('This is file operation')
f.write('\nWe are creating a file')
f.close()
f=open('python.txt','r')
res=f.read()
content=res.replace('This is file operation','This is file I/O operation')
f.close()
print(content)
f=open('python.txt','w')
f.write(content)
f.close()

