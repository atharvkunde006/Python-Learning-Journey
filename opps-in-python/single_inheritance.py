#
from constructor import car


class animal:
    def show(self):
        print("animal makes a sound")
class dog(animal):
    def show1(self):
        print("my dog is good")
s1=dog()
s1.show()
s1.show1()

##
class vehical:
    def __init__(self,brand):
        self.brand=brand
        
    def show(self):
            print(f"The {self.brand} is my favorit brand")
            
class model(vehical):
        def __init__(self,brand,car):
         super().__init__(brand)
         self.car=car
        
        def detailes(self):
           print(f" The {self.brand} is my favorit and the car is{self.car}")
            
s1=vehical("toyota")
s1.show()
s2=model("fortuner")
s2.detailes()