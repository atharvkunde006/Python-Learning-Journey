#
class student:
    def show(self):
        print("This is my student")
        
class parent(student):
    def show(self):
                print("This is my parent")
s1=parent()
s1.show()

##
class student:
    def show (self):
        print("This is my helicopter")
        
class parent(student):
    def show(self):
            super().show()
            print("this is my aroplane")
s1=parent()
s1.show()

###
class shape:
    def __init__(self,x,y):
     self.x=x
     self.y=y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):
            return 3.14*super().area()
c=circle(5)                
print(c.area())