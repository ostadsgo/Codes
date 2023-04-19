void main() {
  print("Hello World!");

  // Declare string
  var name = "John Doe";
  print("My name is " + name);

  // declare integers
  var x = 10;
  var y = 20;
  // string interopolation
  print("$x + $y = ${x + y}");

  // dynamic when you don't know about type.
  dynamic unknowType = "something";
  print("Unknow type $unknowType");

  // const and final
  // const ment for compile time
  // final ments for runtime.
  const pi = 3.14159265;
  final a = 'a';

  var someVariable;
  someVariable = 10;
  someVariable = "hello world";
  print(someVariable);
}
