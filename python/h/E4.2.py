def play(word, position, board):
    direction = position[0]
    line = position[1]
    column = position[2]

    if direction == 'H':
        for i in range(len(word)):
            board[line][column + i] = word[i]
    elif direction == 'V':
        for i in range(len(word)):
            board[line + i][column] = word[i]
