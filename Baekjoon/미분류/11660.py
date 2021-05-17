from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

A = []
for n in range(N):
    A.append(list(map(int, input().split())))

SUMS = [[0 for _ in range(N+1)]]
for r in range(N):
    temp = [0]
    for c in range(N):
        temp.append(temp[-1] + A[r][c])
    SUMS.append(temp)

    for c in range(N):
        SUMS[r+1][c+1] += SUMS[r][c + 1]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(SUMS[x2][y2] - SUMS[x1-1][y2] - SUMS[x2][y1-1] + SUMS[x1-1][y1-1])