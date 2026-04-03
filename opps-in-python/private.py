#
class student:
    def __init__(self):
        self.__name="Atharv"
        
    def show(self):
            print(self.__name)
s1=student()
print(s1.__name) # this will throws error direct access
s1.show()#this will work because we call method


##
class student:
    def __init__(self):
        self.__name= "atharv"
        
    def show(self):
        print(self.__name)
s1=student()
print(s1._student__name) # this can be run becouse of name mangling