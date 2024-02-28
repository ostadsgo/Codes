def check_answer(corr_ans, user_ans):
    if corr_ans == user_ans:
        return True
    else:
        attempt = 0
        while attempt < 2:
            ans = input("Sorry, wrong answer. Try again. ")
            if corr_ans == ans:
                return True
            attempt += 1
    return False


score = 0
print("Guess the Animal!")


running = True
while running:
    ans = input("Which live at the North Pole? ")
    if check_answer("polar bear", ans):
        print("correct answer")
        score += 1

    ans = input("Which is the largest animal? ")
    if check_answer("whale", ans):
        print("correct answer")
        score += 1

    ans = input("Which is the fastest animal? ")
    if check_answer("cheetah", ans):
        print("correct answer")
        score += 1

    print(f"Your score is {score}")
    running = False
