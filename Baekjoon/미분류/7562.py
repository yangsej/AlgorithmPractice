from collections import deque

DIRS = [[-2, 1], [-2, -1], [-1, -2], [-1, 2], [1, 2], [1, -2], [2, 1], [2, -1]]

T = int(input())
for t in range(T):
    I = int(input())

    sr, sc = map(int, input().split())
    dr, dc = map(int, input().split())

    visit = [[0] * I for _ in range(I)]
    queue = deque([[sr, sc]])
    while queue:
        r, c = queue.popleft()
        if r == dr and c == dc:
            print(visit[dr][dc])
            break

        for x, y in DIRS:
            nr = r + x
            nc = c + y

            if 0 <= nr < I and 0 <= nc < I:
                if not visit[nr][nc]:
                    visit[nr][nc] = visit[r][c] + 1
                    queue.append([nr, nc])
