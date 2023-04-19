void main() {
  // List
  var ages = [19, 18, 11, 18, 17];
  print(ages);
  print(ages[0]);

  ages[0] = 100;
  print(ages[0]);

  // empty list
  var names = [];
  names.add("John");

  // add multiple things
  names.addAll(["Jeff", "Marry"]);
  print(names);

  // insert xth position.
  names.insert(0, "Bob");
  // can add numbers too!
  names.insert(1, 3.14);
  int result = add(2, 3);
  print("The result is $result");
}

int add(int x, int y) {
  return x + y;
}
