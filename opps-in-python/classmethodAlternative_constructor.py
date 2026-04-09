#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
    
p1 = Person.from_string("john,30")

print(p1.name)  
print(p1.age)   


##
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        name, salary = string.split("-")   
        return cls(name, int(salary))


e1 = Employee("harry", 12000)
print(e1.name)
print(e1.salary)

string = "john-12000"
e2 = Employee.from_string(string)

print(e2.name)
print(e2.salary)


###
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def from_string(cls,string):
            name, marks = string.split("-")
            return cls(name, int(marks))
s1=student("atharv",90)
print(s1.name)
print(s1.marks)
string="shyam-80"
s2=student.from_string(string)
print(s2.name)
print(s2.marks)

####
class student:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_string(cls,string):
            name,salary,_=string.split("-")
            return cls(name,int(salary))
s1=student("parth",12000)
print(s1.name)
print(s1.salary)
string="kiran-15000-12"
s2=student.from_string(string)
print(s2.name)
print(s2.salary)
