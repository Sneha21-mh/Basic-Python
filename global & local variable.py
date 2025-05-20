#example 1
x=10
def f1():
    x=20
    print(x)
    print(globals()['x'])
f1()

print("")
#example 2
x=10
y=20
def f2():
    y=30
    print(x)
    print(y)
    print(globals()['x'])
    print(globals()['y'])
f2()