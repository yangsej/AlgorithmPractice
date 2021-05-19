from collections import deque

answer = 0

M, N = map(int, input().split())

A = []
for m in range(M):
    A.append(list(map(int, input().split())))

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
visit = [[False] * N for _ in range(M)]
queue = deque()
for m in range(M):
    for n in range(N):
        if not visit[m][n]:
            visit[m][n] = True
            if A[m][n]:
                queue.append([m, n])
                while queue:
                    r, c = queue.popleft()

                    for x, y in DIRS:
                        nr = r + x
                        nc = c + y

                        if 0 <= nr < M and 0 <= nc < N:
                            if not visit[nr][nc]:
                                visit[nr][nc] = True
                                if A[nr][nc]:
                                    queue.append([nr, nc])
                answer += 1
print(answer)