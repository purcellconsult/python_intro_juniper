"""
An example of inheritance in python
-----------------------------------
The base class is the parent class, and
all of it's subclasses are the children classes.
In this case the
"""

class Pet:
    """
    This is a simple class that
    models a pet.
    """
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Yawn")

    def food(self):
        print("Apples")

    def is_sleeping(self):
        return False


class Dog(Pet):
    def sound(self):
        print("Woof!")

    def food(self):
        print("Pedigree")


class Snoppy(Dog):

    def food(self):
        print("pizza")

    def temperament(self):
        print('happy')

    def is_popular(self):
        print(True)


d1 = Dog('charlie')
d1.sound()
d1.food()
print(d1.is_sleeping())

d2 = Snoppy('snoppy')
d2.sound()
d2.food()
d2.temperament()
d2.is_popular()

# need to add a method that you want to be added for all of them later?
# Simple, just add it to the base class

