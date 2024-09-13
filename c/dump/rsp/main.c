#include <stdio.h>
#include <stdlib.h>
#include <time.h>

enum Hand { ROCK, PAPER, SCISSORS };
enum Outcome { WIN, LOSE, DRAW };

enum Outcome decideOutcome(enum Hand userHand, enum Hand computerHand) {
  enum Outcome outcome;
  if (userHand == ROCK && computerHand == PAPER)
    outcome = LOSE;
  else if (userHand == ROCK && computerHand == SCISSORS)
    outcome = WIN;
  else if (userHand == PAPER && computerHand == ROCK)
    outcome = WIN;
  else if (userHand == PAPER && computerHand == SCISSORS)
    outcome = LOSE;
  else if (userHand == SCISSORS && computerHand == ROCK)
    outcome = LOSE;
  else if (userHand == SCISSORS && computerHand == PAPER)
    outcome = WIN;
  else
    outcome = DRAW;

  return outcome;
}

enum Hand getUserHand() {
  int userChoice;
  printf("1: Rock\n2: Paper\n3: Scissors\n");
  printf("Choose 1, 2 or 3\n");
  printf("> ");
  scanf("%d", &userChoice);
  userChoice--;
  if (userChoice < 0 || userChoice > 2) {
    return -1;
  }
  return (enum Hand)userChoice;
}

enum Hand getRandomHand() {
  srand(time(NULL));
  return (enum Hand)rand() % 3;
}

void printWinner(enum Hand userHand, enum Hand compHand, enum Outcome outcome) {
  if (userHand == ROCK && compHand == PAPER) {
    printf("ROCK --VS-- PAPER\n");
    printf("Paper covers Rock\n");
  } else if (userHand == PAPER && compHand == ROCK) {
    printf("PAPER --VS-- ROCK\n");
    printf("Paper covers Rock\n");
  } else if (userHand == ROCK && compHand == SCISSORS) {
    printf("ROCK --VS-- SCISSORS\n");
    printf("Rock crushes Scissors\n");
  } else if (userHand == SCISSORS && compHand == ROCK) {
    printf("SCISSORS --VS-- ROCK\n");
    printf("Rock crushes Scissors");
  } else if (userHand == PAPER && compHand == SCISSORS) {
    printf("PAPER --VS-- SCISSORS\n");
    printf("Scissors cuts Paper\n");
  } else if (userHand == SCISSORS && compHand == PAPER) {
    printf("SCISSORS --VS-- PAPER\n");
    printf("Scissors cuts Paper\n");
  } else { // draw
    if (userHand == 0) {
      printf("ROCK --VS-- ROCK\n");
    } else if (userHand == 1) {
      printf("PAPER --VS-- PAPER\n");
    } else if (userHand == 2) {
      printf("SCISSORS --VS-- SCISSORS\n");
    } else {
      printf("");
    }
  }

  switch (outcome) {
  case (WIN):
    printf("You WIN\n");
    break;
  case (LOSE):
    printf("You LOSE\n");
    break;
  case (DRAW):
    printf("It is a DRAW.\n");
    break;
  }
}

void showStat(int userWinNumber, int computerWinNumber, int drawNumber) {
  printf("----------------------\n");
  printf("User Win: %d\n", userWinNumber);
  printf("Computer Win: %d\n", computerWinNumber);
  printf("Draw Number: %d\n", drawNumber);
  printf("----------------------\n");
}

void play(enum Hand userHand, enum Hand computerHand, enum Outcome outcome) {
  int userWinNumber = 0;
  int computerWinNumber = 0;
  int drawNumber = 0;

  for (int i = 0; i < 10; i++) {
    system("clear");
    userHand = getUserHand();
    computerHand = getRandomHand();
    outcome = decideOutcome(userHand, computerHand);
    if (userHand == -1) {
      printf("ERROR: Invalid choice.\nNext time enter 1, 2, or 3\n");
    } else {
      printWinner(userHand, computerHand, outcome);
      switch (outcome) {
      case WIN:
        userWinNumber++;
        break;
      case LOSE:
        computerWinNumber++;
        break;
      case DRAW:
        drawNumber++;
        break;
      }
    }

    printf("Prsss ENTER key to continue ...");
    getchar();
    getchar();
  } // end for
  // show stat
  showStat(userWinNumber, computerWinNumber, drawNumber);
}

int main() {
  enum Hand userHand;
  enum Hand computerHand;
  enum Outcome outcome;
  play(userHand, computerHand, outcome);
  return 0;
}
