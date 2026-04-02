class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound1(self):
        print("animal makes sound")
class mamal:
    def __init__(self,name,for_color):
        self.name=name
        self.for_color=for_color
        
class dog(animal,mamal):
    def __init__(self,name,breed,for_color):
        animal.__init__(self,name,species="Canine")
        mamal.__init__(self,name,for_color)
        self.breed=breed
    def make_sound(self):
            print(f"{self.name} is my {self.breed} dog and it is {self.for_color} dog")

s1=dog("simba","dobberman","black")
s1.make_sound1()
s1.make_sound()