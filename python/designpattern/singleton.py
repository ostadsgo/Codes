class Person:
    object_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if Person.object_num > 0:
            raise ValueError("Cannot create new object. Person is Singleton.")
        Person.object_num += 1
        
p = Person("Peter", 12)
p1 = Person("Peter", 12)
