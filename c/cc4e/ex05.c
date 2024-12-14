#include <stdio.h>


int main() {
  char line[1000];
  printf("Enter line\n");
  /* read until end of line; match anything rather than new line. */
  fgets(line, 1000, stdin);
  printf("Line: %s\n", line);
}
