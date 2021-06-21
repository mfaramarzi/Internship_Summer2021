import numpy as np
import sys

M = int(sys.argv[1])
N = int(sys.argv[2])

count = 0

for i in range(10):
    for centers in [2, 4, 8, 16]:
        board = np.zeros((M,N), dtype=int)
        rows = np.random.randint(0, M, centers)
        cols = np.random.randint(0, N, centers)
        centers = np.column_stack((rows,cols))

        for cx in centers:
            h = int(np.random.randint(0,M)/4)
            w = int(np.random.randint(0,N)/4)
            board[cx[0]-h:cx[0]+h,cx[1]-w:cx[1]+w] = 1

        with open('board-{}-{}-{:03d}.txt'.format(M,N,count), 'wt') as f:
            for b in board:
                f.write(' '.join(map(str,b))+'\n')
        count += 1
