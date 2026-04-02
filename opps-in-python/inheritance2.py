class sandip_university:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def show(self):
            print(f"{self.name}is placed in {self.location}")
class foundation(sandip_university):
                def __init__(self,name,location,department,student):
                    super().__init__(name,location)
                    self.department=department
                    self.student=student
                def show1(self):
                        print(f"{self.department} is my favorite and i am stude {self.student} of sandip university {self.name} and {self.location}")
                        
s1=sandip_university("sandip university","nashik")
s1.show()
s2=foundation("sandip university","nashik","computer engineering","atharv")  
s2.show1()      
            
