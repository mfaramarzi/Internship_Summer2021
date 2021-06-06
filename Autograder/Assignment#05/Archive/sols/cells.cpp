#include <assert.h>
#include <iostream>
#include <fstream>
#include <cstring>

int count_cells(int *A, int M, int N, int X, int Y, int C) {
    if (X < 0 || Y < 0 || X >= M || Y >= N) return 0;
    if (A[N*X+Y] == 0) return 0;

    A[N*X+Y] = 0;

    int count = 1;
    count += count_cells(A, M, N, X-1, Y, C);
    count += count_cells(A, M, N, X+1, Y, C);
    count += count_cells(A, M, N, X, Y-1, C);
    count += count_cells(A, M, N, X, Y+1, C);
    if (C == 8) {
        count += count_cells(A, M, N, X-1, Y-1, C);
        count += count_cells(A, M, N, X+1, Y+1, C);
        count += count_cells(A, M, N, X+1, Y-1, C);
        count += count_cells(A, M, N, X-1, Y+1, C);
    }
    return count;
}

int main(int argc, const char * argv[]) {
    int M, N, X, Y, C;
    std::string fname = argv[1];
    std::ifstream infile;
    infile.open(fname);

    M = std::atoi(argv[2]);
    N = std::atoi(argv[3]);
    X = std::atoi(argv[4]);
    assert(X <= M && X > 0);
    Y = std::atoi(argv[5]);
    assert(Y <= N && Y > 0);
    C = std::atoi(argv[6]);
    assert(C == 4 || C == 8);

    int *array = new int [M*N];
    int k = 0;
    for (int i = 0 ; i < M ; i ++) {
        for (int j = 0 ; j < N ; j ++) {
            infile >> array[k++];
        }
    }
    assert(k == (M*N));

    std::cout << count_cells(array, M, N, X-1, Y-1, C) << std::endl;

    delete [] array;

    infile.close();

    return 0;
}
