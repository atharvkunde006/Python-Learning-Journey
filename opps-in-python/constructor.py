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

####
class person:
    def __init__(self,name,occ):
        print("he i am person")
        self.name=name
        self.occ=occ
    def info(self):
             print(f"i am a {self.name} and i am work in {self.occ}")
s1=person("atharv","banglore")
s2=person("sham","pakistan")
s1.info()
s2.info()

###### Rectangle area
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
            print(f"Area is : {self.length*self.width}")
s1=rectangle(20,4)
s1.area()

####### default constrctor
class person:
    def __init__(self):
        print("self.name self.age")
s1=person()

####### Employee
class Employee:
    def __init__(self,id, name, salary):
        self.id=id
        self.name=name
        self.salary=salary
    def details(self):
            print(f"my id is {self.id} my name is {self.name} and my salari is{self.salary}")
s1=Employee(1515,"Atharv",10000)


s1.details()

######## conditional constructor
class Bank:
    def __init__(self, balance):
        if balance < 0:
            print("Invalid Balance")
        else:
            self.balance = balance

b = Bank(-100)
b= Bank(100)