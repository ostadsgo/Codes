#include <stdio.h>
#include <stdlib.h>

int main() {
  int num, sum = 0;
  float ave;
  const int n = 5;

  system("clear");

  for (int i = 0; i < n; i++) {
    printf("Enter number %d :", i + 1);
    scanf("%d", &num);
    sum += num;
  }
  ave = (float)sum / n;
  printf("\n the average is: %6.2f", ave);
  getchar();

  return 0;
}
