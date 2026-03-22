#
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
            print(f"The name of Employee:{self.id} is {self.name}")
            
class programmer(Employee):
     def showlanguage(self):
       print("The default language is python")
                
s1=Employee("Rohan Das",400)
s1.show()
s2=programmer("Harry",4100)
s2.show()
s2.showlanguage()

##
class vehical:
    def __init__(self,brand):
        self.brand=brand
        
    def show(self):
        print(f"The brand is {self.brand}")
        
class detail (vehical):
    def __init__(self,brand,model):
        super(). __init__(brand)
        self.model=model
        
    def s1(self):
        print(f"The brand is {self.brand} and car is{self.model}")
s1= detail("toyota","fortuner")
s1.show()
s1.s1()

###
class animal():
    def  __init__(self,sound):
        self.sound=sound
        
    def show(self):
            print("animal makes a ",self.sound)
            
class dog(animal):
         def __init__(self,sound,barks):
                      super().__init__(sound)
                      self.barks=barks
                    
         def detail(self):
           print("dog",self.barks)

s1=dog("sound","barks")
s1.show()
s1.detail()

###
class grandfather():
    def __init__(self,name):
        self.name=name
        
    def show(self):
            print(f"My name is: {self.name} i am grandpa.")
class father():
    def __init__(self,name1):
        self.name1=name1
        
    def show1(self):
        print(f" {self.name1} is my child .")

class child(grandfather,father):
    def __init__ (self,name,name1,name3):
        grandfather.__init__(self,name)
        father.__init__(self,name1)
        self.name3=name3
        
    def show2(self):
            print(f"{self.name3} is my grandchild")
s1=child("Atharv","Shyam","Vinit")
s1.show()
s1.show1()
s1.show2()