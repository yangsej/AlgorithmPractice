from collections import deque

DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

N, M, T = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

queue = deque([[0, 0]])

visit = [[-1] * M for _ in range(N)]
visit[0][0] = 0
answer = N * M
while queue:
    x, y = queue.popleft()

    for dx, dy in DIRS:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] < 0 and A[nx][ny] != 1:
                visit[nx][ny] = visit[x][y] + 1
                if A[nx][ny] == 2:
                    answer = visit[nx][ny] + N + M - nx - ny - 2
                queue.append([nx, ny])
answer = min(answer, visit[N-1][M-1])
if answer > T or answer < 0:
    print("Fail")
else:
    print(answer)