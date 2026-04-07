#
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
            print(f"my name is {self.name} and my age is {self.age}")
s1=student("atharv",20)
s1.info()

##
class myclass:
    def __init__(self,name):
        self.name=name
    def info(self):
            print(f"my name is {self.name}")
s1=myclass("atharv")
s2=myclass("Shyam")
s1.info()
s2.info()
