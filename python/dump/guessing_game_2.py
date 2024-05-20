from random import randrange


def get_user_guess() -> int:
    user_guess = input("You Guess :> ")
    guess = 0
    if user_guess.isdigit():
        guess = int(user_guess)
    else:
        print("It is not a guess")
    return guess


def compare(value1, value2):
    if value1 > value2:
        return 1
    elif value1 < value2:
        return -1
    else:
        return 0


def compare_guess(user_guess, rand_number):
    # Compare user input with random number.
    result = compare(user_guess, rand_number)
    if result == 1:
        print("Try lower.")
    if result == -1:
        print("Try higher")
    if result == 0:
        print("You win.")



rand_number = randrange(2, 100)
print("I am number between 1 to 99")
print("Try to guess me.")


for i in range(10):
    user_guess = get_user_guess()
    if not user_guess:
        continue

    res = compare_guess(user_guess, rand_number)
    if res == 0:
        print(f"It tooks {i} times.")
        break
else:
    print("You didn't win.")
