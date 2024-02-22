def readinput(filename: str):
    with open(filename) as file:
        content = file.read().strip().split("\n")
    return content


POSSIBLE_CUBE_COUNT = {"red": 12, "green": 13, "blue": 14}

RESULT = 0


def is_game_possible(line: str) -> bool:
    subgames = line.split(":")[1].split(";")
    for subgame in subgames:
        for num_cubes in subgame.split(","):
            num, color = num_cubes.split()
            if int(num) > POSSIBLE_CUBE_COUNT[color]:
                return False
    return True


INPUT = readinput("input.txt")
for index, line in enumerate(INPUT, 1):
    if is_game_possible(line):
        print(f"Game {index} is possible")
        RESULT += index

print(RESULT)
