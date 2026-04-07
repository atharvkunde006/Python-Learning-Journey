#
from unicodedata import name


from unicodedata import name


class myclass:
    class_variable=0
    def __init__(self):
        myclass.class_variable+=1
    def print_class_variable(self):
        print(myclass.class_variable)
obj1=myclass()
obj2=myclass()
obj1.print_class_variable()
obj2.print_class_variable()

##
class myclass:
    student = "atharv"

    def __init__(self, rollno):
        self.rollno = rollno
        
    def info(self):
        print(self.rollno)

s1 = myclass(1515)
s2 = myclass("atharv")   # fixed

s1.info()                # fixed
print(s2.student)

###
class myclass:
    student="shivaji maharaj"
    def __init__(self,rollno):
        self.rollno=rollno
s1=myclass("kartik")
s2=myclass(5)
print(s1.student)
print(s2.student)

####
class Employee:
    companyname = "apple"
    noofemployees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noofemployees += 1

    def showdetails(self):
        print(f"My name is {self.name} and I am working in {Employee.companyname} and my raise amount is {self.raise_amount}")

s1 = Employee("Atharv")
s2 = Employee("Rahul")
s2.raise_amount = 0.3
s1.showdetails()
s2.showdetails()