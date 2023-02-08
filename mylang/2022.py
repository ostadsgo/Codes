// comment

// constant defenition
// constant must hanve value
// known at compile time
// no need to add type 
NAME :: "John Doe";

// Variable
// with defualt value
age : int = 10;
age += 1;

// type inference
age := int(input("Enter your age: "));
age += 1;

// use default value of int
age : int;

x, y: int;
x: int, y: int: y, x;

result := if x > 0 {x;} else {y;}
// idea
result := if x > 0: x; else: y;

msg := "My name is {name} and I am {age} years old";
info : dict[str, int] = ["age": 12, "name": "John"];
msg := "My name is {name} and I am {age} years old".format(**info);

upper_name := name.upper();
lower_name := name.lower();

// Arrays
// fixed length same type;

arr : array[int; 5] = [1, 2, 3];
arr.append(4);

arr[0];  // 1

arr[0..2]  // 1, 2
arr[..2]   // 1, 2
arr[2..]   // 3, 4
arr[..]    // copy of arr
arr[-1]    // last item
arr[-1..-3] // last 3 items 4, 3
arr[-1..]
arr[..-3]
arr[1....2] // problem !!! steps 


/* Function */
add :: (x: int, y: int) -> int {
    return x + y;
}

add(2, 3);  /* 5 */

add_one :: (x:int) -> int {
    add :: (a: int, b: int) -> int {
        return a + b;
    }
    return add(1, n);
}


(x: int, y: int) => x + y;
add :: (x: int, y: int) -> int {return x + y;}

result : string;
x := 5

if x > 0 {
    result = "positive";
}
else if x < 0 {
    result = "negative";
}
else {
    result = "zero";
}



result := if x > 0 {
    "positive";
}
else if x < 0 {
    "negative";
}
else {
    "zero";
}


result := if x > 0 { "positive"; }
else if x < { "negative"; }
else { "zero"; }

/* block expression
result := {
    x: int;
    y: float = 1.4;
    x +  y;
    lst: List[str|int|float] = [1, 2, 3, 'hello', 1.1, 0.0]
    x + y + lst.length;
}


/* modules are like class but you canot make object from them. */

Person :: module {
    
}

Person.walk();




main :: package();

os :: import("core/os");
fmt :: import ("core/format");

os.rmdir("./nasty_images");
version := os.version;  // os.version();


x : int = 20;


export(x, y, z);

/* infite loop */
for {

}

for true {}


for i < 10 {
}


for names {
    print(it);
}


for it in names {
    print(it);
}


for range(10) {
    print(it + 2);
}


for number in range(10) 
    print(number + 2);

names := ["John", "Jeff", "Marry"];
for index, name in enumerate(names, 1)
    print(index, name);

for index, name in names.enumerate(1)
    print(index, name);


int_number : type = type(array[int])
matrix := type(array);
Martix := array([[1, 2, 3], [1,2 ,3 ]]);

x : int = int('123');

mx : matrix[float|int; 12] = [[1, 2, 3], [1, 2, 3]];

msg := type(string | int);
result : tuple[name: msg] = [msg: 'not found', error: 404];

Person := type(name: string, age: int, id: string);
peter: Person;
peter.name = "Peter Parker";
peter.age = 23;
peter.id = "23234234234";

Number := alias(int);

add2 := (x: int, y: int) => x + y;

add := alias(add2);

