// import libarary

import "dart:io";

void main() {
  print("Enter number one: ");
  // readLIneSync return nullable String which indicated String?
  String? numberOne = stdin.readLineSync();
  print("Enter number two: ");
  String? numberTwo = stdin.readLineSync();
  int num1 = int.parse(numberOne ?? '0');
  int num2 = int.parse(numberTwo ?? '0');
  int result = add(num1, num2);
  print("$numberOne + $numberTwo = $result");
}

int add(int x, int y) {
  return x + y;
}
