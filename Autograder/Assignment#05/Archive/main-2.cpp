#include "cellgrid.h"
#include <iostream>

int main(int argc, char *argv[]) {
    int M, N, conn;
    char *fname = argv[1];
    
    M = atoi(argv[2]);
    N = atoi(argv[3]);
    conn = atoi(argv[4]);

    Cellgrid myGrid(fname, M, N);
    std::cout << myGrid.countBlobs(conn) << std::endl;

    return 0;
}