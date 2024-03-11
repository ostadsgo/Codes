#include <stdio.h>
#include <stdlib.h>


int main() {
  char ch;
  system("clear");

  for (ch='a'; ch <= 'f'; ch ++ )
      printf("ch = %c, code = %d\n", ch, ch);

  getchar();
  return 0;
}
