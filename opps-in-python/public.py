#
class student:
    def __init__(self,name):
        self.name=name
s1=student("atharv")
print(s1.name)

##
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def info(self):
            print(f"name:{self.name} & salary:{self.salary}")
            
s1=Employee("sham",20000)
print(s1.name)
s1.info()

###
