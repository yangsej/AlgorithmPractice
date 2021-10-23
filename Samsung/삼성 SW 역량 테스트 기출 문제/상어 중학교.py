DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

answer = 0
while True:
    # 그룹 탐색
    visit = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if visit[i][j]: continue
            if A[i][j] <= 0: continue

            visit[i][j] = True
            groups.append([[], [(i, j)]])
            group = groups[-1]
            rainbows, queue = group

            index = 0
            length = 1
            color = A[i][j]

            while index < length:
                r, c = queue[index]
                index += 1

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                    if visit[nr][nc]: continue

                    if color == A[nr][nc]:
                        visit[nr][nc] = True
                    elif A[nr][nc] == 0:
                        visit[nr][nc] = True
                        rainbows.append((nr, nc))
                    else:
                        continue

                    queue.append((nr, nc))
                    length += 1

            if len(queue) == 1:
                groups.pop()

            for r, c in rainbows:
                visit[r][c] = False

    if not groups: break

    # 그룹 선택
    index = -1
    length = -1
    rainbow = -1
    L = len(groups)
    for i in range(L):
        group = groups[i]
        rainbows, coords = group
        cl = len(coords)
        rl = len(rainbows)

        if length < cl or (length == cl and rainbow <= rl):
            length = cl
            index = i
            rainbow = rl

    # 점수 계산
    answer += length * length
    group = groups[index]
    rainbows, coords = group
    for r, c in coords:
        A[r][c] = -2

    # 중력
    pass
    for c in range(N):
        for r in range(N-1, 0, -1):
            if A[r][c] != -2: continue

            for nr in range(r-1, -1, -1):
                if A[nr][c] == -1: break
                elif A[nr][c] == -2: continue
                else:
                    A[r][c] = A[nr][c]
                    A[nr][c] = -2
                    break

    # 반시계 회전
    pass
    NA = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            NA[N-1-c][r] = A[r][c]
    A = NA

    # 중력
    pass
    for c in range(N):
        for r in range(N - 1, 0, -1):
            if A[r][c] != -2: continue

            for nr in range(r - 1, -1, -1):
                if A[nr][c] == -1:
                    break
                elif A[nr][c] == -2:
                    continue
                else:
                    A[r][c] = A[nr][c]
                    A[nr][c] = -2
                    break

print(answer)