#include <stdio.h>


int main() {
	int result, kg;
	printf("Enter weight in KG: ");
	scanf("%d", kg);
	result = kg * 1000;
	printf("Weight in germ: %d\n", result);
	return 0;
}

