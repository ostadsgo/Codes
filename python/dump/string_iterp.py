"""
Embed or insert values or objects into your strings so you can build new strings dynamically.
1. The modulu operator % (out dated)
2. str.format
3. f string

To dynamically interpolate a value into a string, you need something called replacement fields
or placeholder which is the curl braces {}

name := "John";
age := 25;

message :: "My name is {name} and I am {age} years old.";

str :: import("string");
str.contains(message, "name");  

message.contains("name");


Method over functions.


isevenv :: (n: int) => n % 2 == 0;
}

person :: struct {
    name: string;
    age: int;
}

person.is_adult :: (self) => self.age >= 18;

numbers = [1, 2, 3, 4, 5];
result :: numbers.apply(it => it % 2);
result :: numbers.apply(it % 2);


1) format function
name = "John"
age = 42
s = "My name is {}, and I am {} years old.".format(name, age);

s = "My name is {1}, and I am {0} years old.".format(age, name);

s = "My name is {user_name}, and I am {user_age} years old.".format(user_age=age, user_name=name);

BNF format string interpolation:
[field_name]
[!conversion]
[: fromat spec]

conversion fields:
    !s => str
    !r => repr
    !a => ascii





"""
