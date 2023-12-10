# day 2
# Combination

possible_cube_count = {"red": 12, "green": 13, "blue": 14}


def readinput(filename: str):
    with open(filename) as file:
        content = file.read().strip().split("\n")
    return content


# extract game id and records
games = []
lines = readinput("input.txt")
for line in lines:
    game = {}
    game_id, sets = line.split(":")
    game["id"] = int(game_id.split()[-1])
    game["sets"] = sets.split(";")
    games.append(game)

sum_id = 0
flag = False
game_id = 1
subgames = [game.get("sets") for game in games]
# for item in subgames:
#     for color in item:
#         num, name = color.split()
#         if int(num) > possible_cube_count[name]:
#             flag = True
#             break
#     else:
#         sum_id += game_id
#
#     game_id += 1
#
#     
#
# print(sum_id)
