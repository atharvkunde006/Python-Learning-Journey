#
x=[1,2,3]
print (dir(x))

##
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person("atharv", 20)
print(p.__dict__)

###
class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(self.name)

help(Student)