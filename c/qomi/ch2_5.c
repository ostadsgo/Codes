#include <stdio.h>



void main() {
	int x;
	float y;
	printf("Enter value of x: ");
	scanf("%d", &x);
	y = 1 / (x ^ 2 + x + 3);
	printf("Result %5.5f\n", y);
}


