#include "cellgrid.h"
#include <iostream>

int main(int argc, char *argv[]) {
    int M, N,row, col, conn;
    char *fname = argv[1];
    
    M = atoi(argv[2]);
    N = atoi(argv[3]);
    row = atoi(argv[4]);
    col = atoi(argv[5]);
    conn = atoi(argv[6]);

    Cellgrid myGrid(fname, M, N);
    std::cout << myGrid.countCells(row, col, conn) << std::endl;

    return 0;
}