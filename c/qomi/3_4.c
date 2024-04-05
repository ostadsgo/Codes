#include <stdio.h>
#include <stdlib.h>

int main() {
  char ch;
  int counter;
  system("clear");
  printf("Enter a statement with . in end: \n");
  for (counter = 0; (ch = getchar()) != '.'; counter++)
    ;
  printf("\nLength of statement is : %d", counter);
  getchar();
  return 0;
}
