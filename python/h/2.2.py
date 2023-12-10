import random

def tire_lettres(support, sac):
    while len(support) < 7 and sac:
        random_index = random.randint(0, len(sac) - 1)
        letter_drawn = sac.pop(random_index)
        support.append(letter_drawn)

