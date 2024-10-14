import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self):
        if self.age <= 0:
            return raise ValueError("Not valid age.")

if __name__ == "__main__":
    peter = Person("Peter Parker", 18)
    peter.set_age()
    
