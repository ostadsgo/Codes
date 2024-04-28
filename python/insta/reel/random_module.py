from random import randrange


rand_number = randrange(1, 100)

is_win = False

for i in range(10):
    user_guess = int(input("Enter your guess: "))
    if rand_number == user_guess:
        print("You win.")
        break
    elif user_guess < rand_number:
        print("Guess higher")
    else:
        print("Guess lower.")
