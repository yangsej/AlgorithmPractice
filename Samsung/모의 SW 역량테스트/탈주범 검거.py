from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    A = []
    for n in range(N):
        A.append(list(map(int, input().split())))

    DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    PIPES = [[], [0, 1, 2, 3], [0, 2], [1, 3], [1, 2], [0, 1], [0, 3], [2, 3]]

    answer = 1
    visit = [[0] * M for _ in range(N)]
    visit[R][C] = 1
    queue = deque([[R, C]])
    while queue:
        r, c = queue.popleft()

        if visit[r][c] == L: continue

        for d in PIPES[A[r][c]]:
            dr, dc = DIRS[d]
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if visit[nr][nc] != 0: continue
            if (d + 2) % 4 not in PIPES[A[nr][nc]]: continue

            answer += 1
            visit[nr][nc] = visit[r][c] + 1
            queue.append([nr, nc])

    print("#%i %i" % (test_case, answer))
