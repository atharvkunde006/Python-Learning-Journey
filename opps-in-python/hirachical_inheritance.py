class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


# Objects
d = Dog("Tommy")
c = Cat("Kitty")
w = Cow("Gauri")

d.show()
d.sound()

print("------")

c.show()
c.sound()

print("------")

w.show()
w.sound()