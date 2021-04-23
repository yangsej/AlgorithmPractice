from collections import deque
from copy import deepcopy

N, M, D = map(int, input().split())

init_enemy = deque()
for n in range(N):
    init_enemy.append(list(map(int, input().split())))

DIRS = [[0, -1], [-1, 0], [0, 1]]
answer = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            count = 0
            enemy = deepcopy(init_enemy)
            for n in range(N):
                archers = [i, j, k]
                targets = []
                for a in archers:
                    V = [[0 for _ in range(M)] for _ in range(N)]
                    V[N-1][a] = 1

                    Q = deque([[N-1, a]])
                    while Q:
                        r, c = Q.popleft()
                        if enemy[r][c] == 1:
                            targets.append([r, c])
                            break

                        for x, y in DIRS:
                            nr = r + x
                            nc = c + y

                            if 0 <= nr < N and 0 <= nc < M:
                                V[nr][nc] = V[r][c] + 1
                                if V[nr][nc] <= D:
                                    Q.append([nr, nc])

                for r, c in targets:
                    if enemy[r][c] == 1:
                        count += 1
                        enemy[r][c] = 0

                enemy.pop()
                enemy.appendleft([0 for _ in range(M)])
            answer = max(answer, count)
print(answer)