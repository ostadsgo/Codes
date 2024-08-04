
with open("input.txt") as file:
    content = [line.strip() for line in file.readlines()]
    print(content)
    total = 0
    max_total = 0
    for line in content:
        if line:
            total += int(line)
        else:
            if total > max_total:
                max_total = total
            total = 0

print(max_total)

