#include <stdio.h>
#include <string.h>

int main() {
  char s[1024];
  scanf("%[^\n]1000", s);
  /* reverse string */
  for (int i = strlen(s); i >= 0; i--) {
    printf("%c", s[i]);
  }
  printf("\n");
}
