#
class student:
    def __init__(self):
        self._name="harry"
    
    def _funcname(self):
        return "code with harry"
    
class subject(student):
    pass

obj=student()
obj1=subject()
print(obj._name)
print(obj1._funcname())

##
class Student:

    def __init__(self):
        self._marks = 85   # protected variable

    def show(self):
        print("Marks:", self._marks)


obj = Student()

# ⚠ Direct access possible (but not recommended)
print(obj._marks)

obj.show()