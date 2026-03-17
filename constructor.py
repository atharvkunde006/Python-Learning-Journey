#
class atharv:
    def __init__ (self,name,age):
        self.name="animal"
        self.age=20
s1=atharv("crab","tortois")
print(s1.name,s1.age)

##
class Student:
    def __init__(self):
        print("Constructor called")

s1 = Student()

###
class car:
    def __init__ (self,brand,value):
        self.brand=brand
        self.value=value
    def info(self):
            print(self.brand,self.value)
s1=car("bmw",2000000)
s1.info()
