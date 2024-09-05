#include <stdio.h>


int main() {
  char line[1000];
  printf("Enter line\n");
  /* read until end of line; match anything rather than new line. */
  scanf("%[^\n]1000s", line);
  printf("Line: %s\n", line);
}
