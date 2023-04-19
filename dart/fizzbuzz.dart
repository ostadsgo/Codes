void main() {
  int i = 0;
  while (i < 100) {
    if (i % 3 == 0 && i % 5 == 0) {
      print("$i : fizzbuzz");
    }
    if (i % 3 == 0) {
      print("$i : Fizz");
    } else if (i % 5 == 0) {
      print("$i : Bazz");
    }
    i++;
  } // end of while
}
