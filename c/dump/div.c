#include <stdio.h>


int div(int x, int y) {
  if (y == 0) 
    return -1;
  else
    return x / y;
}

int main() {
  div(3, 4);
}
