import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for n in range(N)]
count = 0

dif = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()

for n in range(N):
    for m in range(M):
        if arr[n][m] == 1:
            queue.append([n, m])

while queue:
    i, j = queue.popleft()

    for di, dj in dif:
        ni = i + di
        nj = j + dj
        if ni < 0 or nj < 0 or ni >= N or nj >= M: continue
        if arr[ni][nj] != 0: continue
        arr[ni][nj] = arr[i][j] + 1
        queue.append([ni, nj])

    # for a in arr:
    #     print(a)
    # print("=========")

answer = 0
for a in arr:
    if 0 in a:
        answer = 0
        break
    answer = max(answer, max(a))

print(answer - 1)