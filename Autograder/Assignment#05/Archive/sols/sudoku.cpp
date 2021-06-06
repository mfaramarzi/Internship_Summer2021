#include <iostream>
#include <fstream>
#include <string>

void print_board(int board[][9]) {
    for (int i = 0 ; i < 9 ; i ++) {
        std::cout << board[i][0];
        for (int j = 1 ; j < 9 ; j ++) {
            std::cout << ',' << board[i][j];
        }
        std::cout << std::endl;
    }
}

void read_board(std::string& fname, int board[][9]) {
    std::ifstream infile;
    infile.open(fname);
    std::string line;

    for (int i = 0 ; i < 9 ; i ++) {
        std::getline(infile, line);
        for (int j = 0 ; j < 9 ; j ++) {
            board[i][j] = line[j*2] - 48;
        }
    }

    infile.close();
}

bool find_empty_cell(int &r, int &c, int b[][9]) {
    for (r = 0 ; r < 9 ; r ++) {
        for (c = 0 ; c < 9 ; c ++) {
            if (b[r][c] == 0) {
                return true;
            }
        }
    }
    return false;
}

bool is_safe(int b[][9], int r, int c, int d) {
    // check current row and current column
    for (int i = 0 ; i < 9 ; i ++) {
        if (b[r][i] == d || b[i][c] == d) {
            return false;
        }
    }
    // check inside the box
    int ri = r - r % 3;
    int ci = c - c % 3;
    for (int i = 0 ; i < 3 ; i ++) {
        for (int j = 0 ; j < 3 ; j ++) {
            if (b[ri+i][ci+j] == d) {
                return false;
            }
        }
    }
    // safe
    return true;
}

bool solve_board(int board[][9]) {
    int row, col;
    if (! find_empty_cell(row, col, board)) {
        return true;
    }
    for (int d = 1 ; d < 10 ; d ++) {
        if (is_safe(board, row, col, d)) {
            board[row][col] = d;
            if (solve_board(board)) {
                return true;
            } else {
                board[row][col] = 0;
            }
        }
    }
    return false;
}

int main(int argc, const char * argv[]) {
    int board[9][9];
    std::string fname = argv[1];

    read_board(fname, board);
    solve_board(board);
    print_board(board);

    return 0;
}
