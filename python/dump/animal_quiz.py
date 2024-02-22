print("Guess the Animal!")
score = 0


for i in range(2):
    ans = input("Sorry, wrong answer. Try again. ")
    if ans == "polar bear":
        print("Correct answer")
        score += 1
        break

for i in range(2):
    ans = input("Sorry, wrong answer. Try again. ")
    if ans == "cheetah":
        print("Correct answer")
        score += 1
        break

for i in range(2):
    ans = input("Which is the largest animal? ")
    if ans == "whale":
        print("Correct answer")
        score += 1
        break

print("Your score is " + str(score))
