class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def show(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")

class dog(animal):
    def __init__(self,name,breed):
        super(). __init__(name,"Dog")
        self. breed=breed
    def show_detailes(self):
        self.show()
        print(f"Breed:{self.breed}")

class Golden_retriver(dog):
    def __init__(self,name, color):
        super().__init__(name,"Golden Retriver")
        self.color=color
    def show_detailes(self):
                super().show_detailes()
                print(f"color:{self.color}")
s1=animal("simba","dog")
s1.show()
print("--------")
s2=Golden_retriver("simba","golden")
s2.show_detailes()
        