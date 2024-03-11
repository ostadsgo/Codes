
#include <stdio.h>
#include <curses.h>

int main() {
    // Initialize the curses library
    initscr();

    // Clear the screen
    clear();

    // Refresh the screen to show the cleared content
    refresh();

    // Wait for a key press
    getch();

    // Restore the terminal to its normal state
    endwin();

    return 0;
}
