import random
import string


adjectives = [
    "Happy",
    "Bright",
    "Brave",
    "Curious",
    "Enthusiastic",
    "Friendly",
    "Generous",
    "Intelligent",
    "Kind",
    "Patient",
]

nouns = [
    "Apple",
    "Car",
    "Dog",
    "Book",
    "Table",
    "Chair",
    "Sun",
    "Moon",
    "Ocean",
    "Mountain",
]

print("Welcome to password cracker")

response = "y"
while response == "y":
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    pun = random.choice(string.punctuation)
    num = random.randrange(100)
    passwd = adj + noun + str(num) + pun
    print(f"Your new password is: {passwd}")

    response = input("Would you like another password? (y/n)")


