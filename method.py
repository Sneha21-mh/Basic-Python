#Types of methods
class TypesMethods:
    #init method
    def __init__(self):
        print('init method')
    #instance method
    def instance(self):
        print('Instance method')
    #class method
    @classmethod
    def class_method(cls):
        print('Class method')
    #static method
    @staticmethod
    def static_method():
        print('Static method')

t=TypesMethods()
t.instance()
TypesMethods.class_method()
t.class_method()
t.static_method()


#Example
class Assignment:
    x=10
    y=20

    def method_one(self,x):
        self.z=30
        print(a.x)
        print(a.y)
        print(self.z)
        print(x)

    @classmethod
    def method_two(cls,y):
        print(y)
        print(a.x)
        print(a.y)
        
a=Assignment()
a.method_one(50)
a.method_two(40)