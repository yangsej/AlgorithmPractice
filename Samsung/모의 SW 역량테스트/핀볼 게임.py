from collections import deque

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
BLOCKS = [(0, 1, 2, 3), (1, 3, 0, 2), (2, 3, 1, 0), (2, 0, 3, 1), (3, 2, 0, 1), (2, 3, 0, 1),
          (0, 1, 2, 3), (0, 1, 2, 3), (0, 1, 2, 3), (0, 1, 2, 3), (0, 1, 2, 3)] # BLOCKS[블록 번호][오는 방향] = 가는 방향

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0

    N = int(input())
    A = [[0] * (N+2) for _ in range(N+2)]
    wormholes = [[], [], [], [], [], [], [], [], [], [], []]

    for j in range(N+2):
        A[0][j] = 5
        A[N+1][j] = 5
        A[j][0] = 5
        A[j][N+1] = 5

    for i in range(1, N+1):
        tmp = list(map(int, input().split()))
        for j in range(1, N+1):
            A[i][j] = tmp[j-1]
            if 6 <= A[i][j] <= 10:
                wormholes[A[i][j]].append((i, j))

    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i][j] != 0: continue

            for DIR in range(4):
                r, c = i, j
                d = DIR
                dr, dc = DIRS[d]
                nr, nc = r + dr, c + dc

                count = 0
                # visit = [[False] * (N+2) for _ in range(N+2)]
                # visit[r][c] = True
                while True:
                    block = A[nr][nc]
                    if 1 <= block <= 5:
                        count += 1
                    elif 6 <= block <= 10:
                        r, c = nr, nc
                        nr, nc = wormholes[block][0]
                        if r == nr and c == nc:
                            nr, nc = wormholes[block][1]

                    if nr == i and nc == j: break
                    if block == -1: break

                    r, c = nr, nc
                    d = BLOCKS[block][d]
                    dr, dc = DIRS[d]
                    nr, nc = r + dr, c + dc

                answer = max(answer, count)
                    # visit[r][c] = True

    print("#%i %i" % (test_case, answer))