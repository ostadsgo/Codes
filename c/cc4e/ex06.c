#include <stdio.h>

int main() {
  char line[1000];
  FILE *fileptr;
  fileptr = fopen("poem.txt", "r");
  while (fgets(line, 1000, fileptr) != NULL) {
    printf("%s", line);
  }
}
