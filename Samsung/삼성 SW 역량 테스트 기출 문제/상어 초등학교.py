SCORES = (0, 1, 10, 100, 1000)
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

N = int(input())
A = [[] for _ in range(N**2+1)]
Order = []

for _ in range(N*N):
    inp = list(map(int, input().split()))
    i = inp.pop(0)
    for l in inp:
        A[i].append(l)
    Order.append(i)

emptyCount = [[4] * N for _ in range(N)]
for n in range(N):
    emptyCount[0][n] = 3
    emptyCount[n][0] = 3
    emptyCount[N-1][n] = 3
    emptyCount[n][N-1] = 3
emptyCount[0][0] = 2
emptyCount[N-1][0] = 2
emptyCount[0][N-1] = 2
emptyCount[N-1][N-1] = 2

Coords = [[-1, -1] for _ in range(N*N+1)]
for o in Order:
    Avails = []
    NearCount = [[0] * N for _ in range(N)]

    for like in A[o]:
        if Coords[like][0] == -1: continue
        lr, lc = Coords[like]

        for dr, dc in DIRS:
            nr, nc = lr + dr, lc + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if emptyCount[nr][nc] < 0: continue

            if NearCount[nr][nc] == 0:
                Avails.append([nr, nc])

            NearCount[nr][nc] += 1


    count = -1
    coord = [-1, -1]
    empty = -1

    Avails.sort()
    for ar, ac in Avails:
        if NearCount[ar][ac] > count or (NearCount[ar][ac] == count and emptyCount[ar][ac] > empty):
            count = NearCount[ar][ac]
            coord = [ar, ac]
            empty = emptyCount[ar][ac]

    if not Avails:
        count = -1
        coord = [-1, -1]
        for r in range(N):
            for c in range(N):
                if emptyCount[r][c] > count:
                    count = emptyCount[r][c]
                    coord = [r, c]


    Coords[o] = coord
    r, c = coord
    emptyCount[r][c] = -1
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc

        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        emptyCount[nr][nc] -= 1


answer = 0

for student in range(1, N*N+1):
    r, c = Coords[student]

    count = 0
    for like in A[student]:
        lr, lc = Coords[like]

        if abs(r - lr) + abs(c - lc) == 1:
            count += 1

    answer += SCORES[count]

print(answer)