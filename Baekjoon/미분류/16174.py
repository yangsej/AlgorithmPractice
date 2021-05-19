from collections import deque

DIRS = [[1, 0], [0, 1]]

N = int(input())

A = []
for n in range(N):
    A.append(list(map(int, input().split())))

answer = "Hing"
visit = [[False] * N for _ in range(N)]
visit[0][0] = True
queue = deque([[0, 0]])
while queue:
    r, c = queue.popleft()

    if r == N-1 and c == N-1:
        answer = "HaruHaru"
        break

    for x, y in DIRS:
        nr = r + x * A[r][c]
        nc = c + y * A[r][c]

        if 0 <= nr < N and 0 <= nc < N:
            if not visit[nr][nc]:
                visit[nr][nc] = True
                queue.append([nr, nc])
print(answer)