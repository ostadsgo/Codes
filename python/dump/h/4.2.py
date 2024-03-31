def play(word, position, board):
    direction, line, column = position

    if direction == 'H':
        for i in range(len(word)):
            board[line][column + i] = word[i]
    elif direction == 'V':
        for i in range(len(word)):
            board[line + i][column] = word[i]
