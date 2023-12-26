from random import randrange

d = {"hello": "salama"}

HAND = 10
RANDOM_NUMBER = randrange(1, 100)

print("I am a number between 1 to 99. Try to guess me.")
while HAND > 0:
    guess = int(input("Enter your guess: "))
    if guess == RANDOM_NUMBER:
        print(f"Congratulation. YOU WIN.")
        break
    elif guess > RANDOM_NUMBER:
        print("Try small number.")
    else:
        print("Try larg number.")

    HAND -= 1

if HAND <= 0:
    print("You didn't win this time :-(")


# this is a comment
def hello():
    return "hello"

"""
"""
hello()
