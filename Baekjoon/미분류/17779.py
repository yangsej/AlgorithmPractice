N = int(input())
A = [[0] * (N+1)]
for n in range(N):
    a = [0] + list(map(int, input().split()))
    A.append(a)

DIRS = [[1, 0], [0, -1], [0, 1]]

answer = 100 * N * N
for x in range(1, N):
    for y in range(2, N):
        for d1 in range(1, min(y, N-x)):
            for d2 in range(1, min(N-y, N-x-d1)):
                visit = [[0] * (N+1) for _ in range(N+1)]
                counts = [0] * 5

                for r in range(d1+d2+1):
                    for c in range(d1+d2):

                for i in range(d1+1):
                    r = x + i
                    c = y - i
                    visit[r][c] = 5
                    counts[4] += A[r][c]

                    r = x + i + d2
                    c = y - i + d2
                    visit[r][c] = 5
                    counts[4] += A[r][c]

                for j in range(d2+1):
                    r = x+j
                    c = y+j
                    visit[r][c] = 5
                    counts[4] += A[r][c]

                    r = x + j + d1
                    c = y + j - d1
                    visit[r][c] = 5
                    counts[4] += A[r][c]

                for r in range(1, N+1):
                    for c in range(1, N+1):
                        if not visit[r][c]:
                            if 1 <= r < x+d1 and 1 <= c <= y:
                                visit[r][c] = 1
                                counts[0] += A[r][c]
                            elif 1 <= r <= x+d2 and y < c <= N:
                                visit[r][c] = 2
                                counts[1] += A[r][c]
                            elif x+d1 <= r <= N and 1 <= c < y-d1+d2:
                                visit[r][c] = 3
                                counts[2] += A[r][c]
                            elif x+d2 < r <= N and y-d1+d2 <= c <= N:
                                visit[r][c] = 4
                                counts[3] += A[r][c]
                answer = min(answer, max(counts) - min(counts))

print(answer)
