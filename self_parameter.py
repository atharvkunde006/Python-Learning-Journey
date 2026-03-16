#
class details:
    name="Atharv"
    age=20
    def desc(self):
        print("My name is",self.name,"and my age is",self.age)
obj1=details()
obj1.desc()

##
class person:
    name="Atharv"
    occupation="software Devloper"
    networth=10
obj=person()
obj.name="shubham"
obj.occupation="Accountant"
print(obj.name,obj.occupation)

###
class person:
    name="atharv"
    occupation="software devloper"
    networth=10
    a=person()
    print(a.name,a.occupation,a.networth)
    
####
class person:
    name="atharv"
    occupation="software Engineer"
    networth=10
    def info(self):
        print(f"{self.name} is a{self.occupation}")
a=person()
a.info()

#####
class person:
    name="atharv"
    occupation="software Engineer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person()
a.name="Abhay"
a.occupation="Data scientist"
a.info()