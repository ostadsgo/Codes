class Person {
  String? name;
  int? age;

  // constractors
  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  void displayInfo() {
    print("Name: ${this.name}\nAge: ${this.age}");
  }
} // end Person

void main() {
  Person peter = Person("Peter Parker", 23);
  peter.displayInfo();
}
