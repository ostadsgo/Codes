print("hello world!")



# class that represent a Person
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_info(self):
        """ A method to print information of a person. """
        print(f"{self.name} {self.age} years old")

    def after_a_year(self):
        return self.age + 1

    def is_a_man(self, gender: str) -> bool:
        if gender == "male":
            return True
        return False



