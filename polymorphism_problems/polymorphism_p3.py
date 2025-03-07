class Animal:
    def make_sound(self):
        return "Animal makes cute sounds"

class Dog(Animal):
    def make_sound(self):
        return "Dog Barks"

class Cat(Animal):
    def make_sound(self):
        return "Cat Meow"

class Cow(Animal):
    def make_sound(self):
        return "Cow Moo"

animal=[Dog(),Cat(),Cow()]
for animal in animal:
    print(animal.make_sound())