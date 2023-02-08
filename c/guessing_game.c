#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int generateRandNumber(int a) {
	srand(time(0));
	return rand() % a; 
}

int playGame(int randomNumber) {
	int userGuess;
	int guessCount = 0;

	while (userGuess != randomNumber) {
		guessCount ++;
		printf("> ");
		scanf("%d", &userGuess);
		if (userGuess > randomNumber)
			printf("Try smaller!\n");
		else if (userGuess < randomNumber)
			printf("Try bigger!\n");
		else {
			printf("Yay you win with %d tries.\n", guessCount);
			return guessCount;
		}
	} // end of while loop.
} // end of playGame function.

void main() {
	int randomNumber = generateRandNumber(100);
	char ans;

	printf("I am a random number between 0 to 100\n");
	printf("Would you like to guess me (y/n): ");
	scanf("%c", &ans);

	if (ans == 'y') {
		printf("Okey let's play.\n");
		printf("Enter your guess: \n");
		playGame(randomNumber);
	}
	else {
		printf(":-(");
		printf("bye");
	}

} // end of main function.
