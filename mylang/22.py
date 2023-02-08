/* varaible declaration */
name := "John Doe";
name: string;

name := 10  /* error */


number := type(x: int, y: int);
person_id := alias(int | string);
number := int | str;
matrix := List[int | float];

/* + - / // * ** % */

Person := class(name, age) {
    walk := (self) => 0;
}

peter = Person("John Doe", 12);
peter.name;  // John Doe
peter.walk();

Number := alias(int|float);
Numbers := alias([int|float]);
lst: list[Number] = [1, 1.1, 2, 2.2];
lst: Numbers = [1, 1.1, 2, 2.2];


/* list */
lst: list[Number] = [1, 1.1, 2, 2.2];
lst.append(10);

/* dict */
person: dict[string, string | age] = ["name": "John", "age": 20];

/* set */
nums : set = [1, 1, 1, 1, 2, 2];  /* [1, 2] */

/* tuple */
user := [
    name: string,
    age: int,
];


Perosn := {
        name: string;
        age: int;

}

peter = Person(name="John Doe", age=42);

@method(peter)
check_age := (age: int) -> bool {
        if age <= 0 { return null; }
        peter.age = age;
}

peter.check_age(12);
peter.age; // 12


// operators
// ^ / * ./ + - 
// number guessing game

random = import("random");
// generate random number
rand_number := random.randint(1, 100);
for {
    guess := int(input("Enter a guess: "));
    if guess < rand_number {
        print("Try higher.");
    }
    elif guess > rand_number {
        print("Try lower.");
    } 
    else {
        print("Congrats.");
        break;
    }
}



/* Lambda */
evens = numbers.filter((n) {return n % 2 == 0});
/* ideal */
evens = numbers.filter(n => n % 2 == 0);

