#

class Employee:
    def __init__(self,name ,id,salary):
     self.name=name
     self.id=id
     self.salary=salary
    
    def info(self):
        print(f"my name is {self.name} and my id is{self.id} and my slary is{self.salary}")
        
s1=Employee("atharv",1515,10000)
s1.info()

##
class area:
    def __init__(self,lenght,wigdth):
        self.lenght=lenght
        self.wigdth=wigdth
    def info(self):
            print(f"area is {self.lenght*self.wigdth}")
s1=area(20,2)
s1.info()

###
class person:
    def __init__(self,salary):
        self.salary=salary
    def info(self):
            self.salary=self.salary+0.10*self.salary
            print(f"my salary is :{self.salary}")
s1=person(1000)
s1.info()

###
class sbi:
    def __init__ (self):
        self.deposite=int(input("Enter your deposite amount:"))
        self.widraw=int(input("Enter your withdrawal amount:"))
    def info(self):
            if self.deposite<self.widraw:
                print("not sufficient balance in your accound")
            else:
                print(f"the ramining amount is:{self.deposite-self.widraw}")
                
s1=sbi()
s1.info()

####
class person:
    def __init__(self,name="unknown",age=0):
        self.name=name
        self.age=age
    def info(self):
            print("my name is",self.name, "my age is", self.age)
s1=person("Atharv",20)
s2=person()
s1.info()
s2.info()