
import random 

random_number = random.randrange(1, 20)
name = input("Hell!, What is your name? ")

print(f"Well {name}, I am thinking of a number between 1 and 20.")

guess_count = 0
is_guessed = False
while not is_guessed:
    guess = int(input("Take a guess\n"))
    guess_count += 1

    if guess > random_number:
        print("Your guess is too high.")
    elif guess < random_number:
        print("Your guess is too low.")
    else:
        print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
        is_guessed = True

