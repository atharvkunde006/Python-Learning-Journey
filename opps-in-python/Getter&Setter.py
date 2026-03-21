#
class name():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
     print(self.name,self.age)
s1=name("atharv",20)
s1.info()

##
class name:
    def __init__(self,name,age):
     self.__name=name
     self.__age=age
    
    #getter
    def get_name(self):
     return self.__name
    
    #setter
    def set_name(self,name):
     self.__name = name
        
    def info(self):
        print(self.__name,self.__age)
            
s1=name("atharv",20)
print(s1.get_name())
s1.set_name("rahul")
s1.info()

###
class bank:
    def __init__(self,balance):
        self.balance=balance
        
    def get_balance(self):
            return self.balance
        
    def set_balance(self,amount):
            if amount>=0:
                self.balance=amount
            else:
                print("invalid balance")
s1=bank(5000)
print(s1.get_balance())
s1.set_balance(-5000)
s1.set_balance(3000)
print(s1.get_balance())                


####
class student:
    def __init__(self,name):
        self.name=name
        
    def get(self):
            return self.name
        
    def set(self,name):
            self.name= name
            
s1=student("atharv")
s1.set("rahul")
print(s1.get())

#####
class age:
    def __init__(self,age):
        self.age=age
        
    def get(self):
         return self.age
     
    def set(self,validation):
        if validation>=0:
            self.age=validation
        else:
            print("invalid age")

s1=age(20)
print(s1.get())
s1.set(-9)
print(s1.get())

######
class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")


s1 = Student(80)

s1.marks = 95    # setter call
print(s1.marks)