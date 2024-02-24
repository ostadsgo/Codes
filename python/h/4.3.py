def check_playable(word, position, board):
    direction, line, column = position
    word_length = len(word)
    needed_letters = []

    for i in range(word_length):
        current_line, current_column = line, column

        if direction == 'H':
            current_column += i
        elif direction == 'V':
            current_line += i

        if current_line >= len(board) or current_column >= len(board[0]):
            print("Your word goes out of the board.")
            return []

        current_letter = board[current_line][current_column]

        if current_letter == '':
            needed_letters.append(word[i])
        elif current_letter != word[i]:
            print(f"Your word covers other letters: {current_letter}.")
            return []

    return needed_letters

#
