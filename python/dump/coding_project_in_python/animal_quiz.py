def check_answer(guess, corr_ans):
    global score
    for _ in range(2):
        ans = input(guess)
        if corr_ans.lower() == ans.lower():
            print("Correct answer")
            score += 1
            return True
        else:
            q = "Sorry, wrong answer. Try again. "
            return check_answer(q, ans)

    return False


print("Guess the Animal!")
score = 0


q = "Which bear lives in the North Pole"
if check_answer(q, "polar bear"):
    print("Correct answer")
    score += 1
else:
    ans = input("Sorry, wrong answer. Try again. ")
    if check_answer(q, "polar bear"):
        print("Correct answer")
        score += 1


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
