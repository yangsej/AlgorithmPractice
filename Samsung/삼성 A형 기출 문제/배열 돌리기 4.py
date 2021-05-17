from copy import deepcopy
from itertools import permutations

N, M, K = map(int, input().split())
A = []
for n in range(N):
    A.append(list(map(int, input().split())))

R = []
for k in range(K):
    r, c, s = map(int, input().split())
    R.append([r, c, s])

answer = 0

P = permutations([i for i in range(6)], 6)
for p in P:
    next_A = deepcopy(A)
    for i in p:
        r, c, s = R[i]
        for j in range(s):
            for k in range(-j, j):
                next_A[r-j][c+k] = A[r-j][c+k-1] # U
                next_A[r+k][c+j] = A[r+k-1][c+j] # R
                next_A[r+j][c+k] = A[r+j][c+k+1] # D
                next_A[r-k][c-j] = A[r-k+1][c-j] # L