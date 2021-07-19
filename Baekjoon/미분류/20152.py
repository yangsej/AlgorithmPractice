from collections import deque

DIRS = [[1, 0], [0, 1]]

H, N = map(int, input().split())
M = abs(H - N) + 1

A = [[0] * M for _ in range(M)]
A[0][0] = 1

queue = deque([[0, 0]])
while queue:
    x, y = queue.popleft()

    for dx, dy in DIRS:
        nx = x + dx
        ny = y + dy

        if nx < M and ny < M:
            if ny > nx:
                continue
            else:
                if not A[nx][ny]:
                    A[nx][ny] = A[nx-1][ny] + A[nx][ny-1]
                    queue.append([nx, ny])

print(A[M-1][M-1])