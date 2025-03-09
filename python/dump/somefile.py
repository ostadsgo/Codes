class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def set_age(self, age: int):
        if self.age > 0:
            self.age = age
        self.age = 0

    def set_name(self, name):
        if len(name) > 3:
            self.name = name
        self.name = ""



peter = Person("Peter Parker", 89)
peter.set_age(90)

joe = Person("Joe Doe", 42)
joe.set_agee(43)
