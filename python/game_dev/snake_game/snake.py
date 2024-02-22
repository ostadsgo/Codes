import curses

stdscr = curses.initscr()

curses.noecho()    # Do not print key presses to the screen
curses.cbreak()    # Do not wait for the Enter key
curses.curs_set(0)    # Hide the cursor

y, x = stdscr.getmaxyx()    # Get the size of the console

# Display the current expression
current_expression = ""
stdscr.addstr(0, 0, f"Current expression: {current_expression}")

# Display the current result
current_result = 0
stdscr.addstr(y - 2, 0, f"Current result: {current_result}")

# Handle keypresses
while True:
    # Get the key pressed
    key = stdscr.getch()

    # Handle numbers
    if key >= ord('0') and key <= ord('9'):
        current_expression = current_expression + chr(key)
        stdscr.addstr(0, x - 3, current_expression)

    # Handle operators
    elif key == ord('+') or key == ord('-') or key == ord('*') or key == ord('/'):
        if current_expression != "":
            # Evaluate the current expression
            try:
                current_result = eval(current_expression)
            except ZeroDivisionError:
                stdscr.addstr(y - 2, 0, "Error: division by zero")
                current_expression = ""

            # Update the display
            stdscr.addstr(0, 0, f"Current expression: {current_expression}")
            stdscr.addstr(y - 2, 0, f"Current result: {current_result}")

            # Reset the current expression
            current_expression = ""

    # Handle clear
    elif key == ord('C'):
        current_expression = ""
        current_result = 0

        stdscr.addstr(0, 0, f"Current expression: {current_expression}")
        stdscr.addstr(y - 2, 0, f"Current result: {current_result}")

    stdscr.refresh()
