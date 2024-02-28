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
    ans = input("Which live at the North Pole?\
                \na) polar bear  b) grizly  c) balck bear  d) none\n> ")
    if check_answer("a", ans):
        print("correct answer")
        score += 1

    ans = input("Which is the largest animal? \
                \na) diz  b) viz  c) whale  d)none\n> ")
    if check_answer("c", ans):
        print("correct answer")
        score += 1

    ans = input("Which is the fastest animal? \
                \na) gazal  b) ...  c) cheetah  d)noen\n> ")
    if check_answer("c", ans):
        print("correct answer")
        score += 1

    print(f"Your score is {score}")
    running = False
