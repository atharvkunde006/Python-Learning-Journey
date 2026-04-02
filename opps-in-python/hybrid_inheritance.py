class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no



class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    


class Intern(Student, Employee):   
    def __init__(self, name, age, roll_no, emp_id, duration):
        super().__init__(self, name, age, roll_no)
        self.emp_id=emp_id
        self.duration = duration

    def show_details(self):
        self.show_person()
        print(f"Roll No: {self.roll_no}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Intern Duration: {self.duration}")


i1 = Intern("Atharv", 20, 101, "E500", "6 months")
i1.show_details()