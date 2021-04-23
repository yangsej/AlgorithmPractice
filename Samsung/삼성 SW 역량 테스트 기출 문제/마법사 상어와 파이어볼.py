from collections import deque

N, M, K = map(int, input().split())

arr = [[deque() for m in range(N)] for n in range(N)]
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

for k in range(K):
    visit = deque()
    for r in range(N):
        for c in range(N):
            for i in range(len(arr[r][c])):
                visit.append([r, c])

    while visit:
        r, c = visit.popleft()
        m, s, d = arr[r][c].popleft()
        if d == 0:
            arr[(r-s+N) % N][c].append([m, s, d])
        elif d == 1:
            arr[(r-s+N) % N][(c+s) % N].append([m, s, d])
        elif d == 2:
            arr[r][(c+s) % N].append([m, s, d])
        elif d == 3:
            arr[(r+s) % N][(c+s) % N].append([m, s, d])
        elif d == 4:
            arr[(r+s) % N][c].append([m, s, d])
        elif d == 5:
            arr[(r+s) % N][(c-s+N) % N].append([m, s, d])
        elif d == 6:
            arr[r][(c-s+N) % N].append([m, s, d])
        elif d == 7:
            arr[(r-s+N) % N][(c-s+N) % N].append([m, s, d])

    for r in range(N):
        for c in range(N):
            size = len(arr[r][c])
            if size > 1:
                M, S, D, even = [0, 0, 0, 0]
                while arr[r][c]:
                    m, s, d = arr[r][c].popleft()
                    M += m
                    S += s
                    D += d
                    if d % 2 == 0:
                        even += 1
                M //= 5
                if M != 0:
                    S //= size
                    if even == 0 or even == size:
                        arr[r][c].append([M, S, 0])
                        arr[r][c].append([M, S, 2])
                        arr[r][c].append([M, S, 4])
                        arr[r][c].append([M, S, 6])
                    else:
                        arr[r][c].append([M, S, 1])
                        arr[r][c].append([M, S, 3])
                        arr[r][c].append([M, S, 5])
                        arr[r][c].append([M, S, 7])

answer = 0
for r in range(N):
    for c in range(N):
        while arr[r][c]:
            m, s, d = arr[r][c].popleft()
            answer += m
print(answer)
