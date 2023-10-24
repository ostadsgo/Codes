numbers = "1 77 89 23 8 7"

splited_numbers = numbers.split(" ")


int_numbers = []
for n in splited_numbers:
    int_numbers.append(int(n))



int_numbers = [int(n) for n in splited_numbers]
