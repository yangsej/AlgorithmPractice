N = int(input())
house = [[[0, 0, 0] for i in range(N+1)] for j in range(N+1)]
house[1][2] = [1, 0, 0]
visit = [[False for i in range(N+1)] for j in range(N+1)]
visit[0] = [True for i in range(N+1)]
visit[1][1] = True
visit[1][2] = True

wall = [[False for i in range(N+1)] for j in range(N+1)]

for n in range(1, N+1):
    L = list(map(int, input().split()))
    visit[n][0] = True
    for m in range(1, N+1):
        if L[m-1] == 1:
            visit[n][m] = True
            wall[n][m] = True

PIPES = [[[0, -1]], [[0, -1], [-1, 0], [-1, -1]], [[-1, 0]]]
DIRS = [[0, -1, 0, 2], [-1, -1, 0, 3], [-1, 0, 1, 3]]

for r in range(1, N+1):
    for c in range(1, N+1):
        if not visit[r][c]:
            visit[r][c] = True

            for m, P in enumerate(PIPES):
                valid = True
                for x, y in P:
                    nr = r + x
                    nc = c + y

                    if wall[nr][nc]:
                        valid = False
                        break

                if valid:
                    dx, dy, s, e = DIRS[m]
                    house[r][c][m] = sum(house[r + dx][c + dy][s:e])


print(sum(house[N][N]))