#include "sudoku.h"
#include <iostream>

int main(int argc, char *argv[]) {
    Sudoku game(argv[1]);
    game.solve();
    game.print();
    return 0;
}