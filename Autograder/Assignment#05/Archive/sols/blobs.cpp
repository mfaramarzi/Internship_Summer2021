#include <assert.h>
#include <iostream>
#include <fstream>
#include <cstring>

void zero_cells(int *A, int M, int N, int X, int Y, int C) {
    if (X < 0 || Y < 0 || X >= M || Y >= N) return;
    if (A[N*X+Y] == 0) return;

    A[N*X+Y] = 0;

    zero_cells(A, M, N, X-1, Y, C);
    zero_cells(A, M, N, X+1, Y, C);
    zero_cells(A, M, N, X, Y-1, C);
    zero_cells(A, M, N, X, Y+1, C);

    if (C == 8) {
        zero_cells(A, M, N, X-1, Y-1, C);
        zero_cells(A, M, N, X+1, Y+1, C);
        zero_cells(A, M, N, X+1, Y-1, C);
        zero_cells(A, M, N, X-1, Y+1, C);
    }

    return;
}

int main(int argc, const char * argv[]) {
    int M, N, C;
    std::string fname = argv[1];
    std::ifstream infile;
    infile.open(fname);

    M = std::atoi(argv[2]);
    N = std::atoi(argv[3]);
    C = std::atoi(argv[4]);

    assert(C == 4 || C == 8);

    int *array = new int [M*N];
    int k = 0;

    for (int i = 0 ; i < M ; i ++) {
        for (int j = 0 ; j < N ; j ++) {
            infile >> array[k++];
        }
    }

    assert(k == (M*N));

    int count = 0;
    for (int i = 0 ; i < M ; i ++) {
        for (int j = 0 ; j < N ; j ++) {
            if (array[N*i+j] == 1) {
                zero_cells(array, M, N, i, j, C);
                count ++;
            }
        }
    }
    std::cout << count << std::endl;

    delete [] array;

    infile.close();

    return 0;
}
