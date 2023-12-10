import random

def tire_lettres(support, sac):
    letters_to_draw = min(7 - len(support), len(sac))
    random_drawn_letters = random.sample(sac, letters_to_draw)
    
    for letter in random_drawn_letters:
        support.append(letter)
        sac.remove(letter)
