class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
            self.num+=n
            @staticmethod
            def add(a, b):
                return a+b
a=math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(math.add(3,4))

##
class student:
    @staticmethod
    def info(name,age):
      print(f"my name is {name} and my age is {age}")
print(student.info("atharv",20))