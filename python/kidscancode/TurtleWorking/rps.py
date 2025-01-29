import random


moves = ('r', 'p', 's')
player_wins = ('rs', 'pr', 'sp')
player_score = 0
comp_score = 0
ties_score = 0

while True:
    player_move = input("Your move (q to quit): ")
    if player_move == "q":
        break
    
    comp_move = random.choice(moves)
    
    if comp_move == player_move:
        print("Tie")
        ties_score += 1
    elif player_move + comp_move in player_wins:
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        comp_score += 1
        
    print("\nScore board")
    print("------------")
    print("You wins " + str(player_score) + " times.")
    print("Computer wins " + str(comp_score) + " times.")
    print("Ties " + str(ties_score) + " times.")
    
