from collections import deque

N, M, F = map(int, input().split())

starts = [[0 for i in range(N+2)] for j in range(N+2)]
for n in range(N):
    line = list(map(int, input().split()))
    for m in range(N):
        if line[m] == 1:
            starts[n+1][m+1] = -1

queue = deque([list(map(int, input().split()))])

WAY = [[-1, 0], [1, 0], [0, -1], [0, 1]]
passengers = [None]
for m in range(M):
    sr, sc, er, ec = list(map(int, input().split()))
    starts[sr][sc] = m+1

    passengers.append([sr, sc, er, ec])

passed = 0
visit = [[-1 for i in range(N+2)] for j in range(N+2)]
visit[queue[0][0]][queue[0][1]] = 0
Q = deque()
for p in range(M):
    while queue:
        r, c = queue.popleft()

        if starts[r][c] > 0:
            Q.append([visit[r][c], r, c])

        for x, y in WAY:
            nr = r + x
            nc = c + y

            if 0 < nr <= N and 0 < nc <= N:
                if visit[nr][nc] == -1 and starts[nr][nc] != -1:
                    visit[nr][nc] = visit[r][c] + 1
                    queue.append([nr, nc])

    if Q:
        d, r, c = min(Q)
        sr, sc, er, ec = passengers[starts[r][c]]

        dist = visit[r][c]
        if dist <= F:
            F -= visit[r][c]
        else:
            F = -1
            break

        visit = [[-1 for i in range(N+2)] for j in range(N+2)]
        visit[sr][sc] = 0

        dist = -1

        Q.clear()
        Q.append([sr, sc])
        while Q:
            r, c = Q.popleft()

            if r == er and c == ec:
                dist = visit[er][ec]
                break

            for x, y in WAY:
                nr = r + x
                nc = c + y

                if 0 < nr <= N and 0 < nc <= N:
                    if visit[nr][nc] == -1 and starts[nr][nc] != -1:
                        visit[nr][nc] = visit[r][c] + 1
                        Q.append([nr, nc])
        if dist == -1:
            F = -1
            break
        Q.clear()

        if dist <= F:
            F += dist

            starts[sr][sc] = 0

            visit = [[-1 for i in range(N + 2)] for j in range(N + 2)]
            visit[er][ec] = 0

            queue.append([er, ec])
        else:
            F = -1
            break
    else:
        F = -1
        break

print(F)