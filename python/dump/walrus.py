def without_walrus():
    hippos = 0
    answer = "y"
    while answer == "y":
        hippos += 1
        print(str(hippos) + "blancing hippos!")
        answer = input("Add another hippo? (y/n)")


def with_walrus():
    hippos = 0
    while answer := input("Add another hippo? (y/n)"):
        hippos += 1
        print(str(hippos) + "blancing hippos!")
        if answer == "y":
            continue


with_walrus()
