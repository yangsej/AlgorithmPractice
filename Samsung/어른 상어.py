from collections import deque

N, M, k = map(int, input().split())

arr = [[deque() for i in range(N)] for j in range(N)]
smell = [[[0, 0] for i in range(N)] for j in range(N)]  # id, time
for n in range(N):
    A = list(map(int, input().split()))
    for m in range(N):
        if A[m] > 0:
            arr[n][m].append(A[m])

DIRS = [None, [-1, 0], [1, 0], [0, -1], [0, 1]]
sharks = list(map(int, input().split()))
sharks.insert(0, 0)

priority = [None]
for m in range(M):
    dirs = []  # U D L R
    for i in range(4):
        dirs.append(list(map(int, input().split())))  # 1:U 2:D 3:L 4:R
    priority.append(dirs)

for answer in range(1002):
    if answer == 1001:
        answer = -1
        break
    count = 0
    queue = deque()

    # smoke() check_pos()
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                i = arr[r][c][0]
                count += 1
                smell[r][c] = [i, k]
                queue.append([r, c])
    if count == 1:
        break

    # move()
    while queue:
        r, c = queue.popleft()

        i = arr[r][c].popleft()
        d = sharks[i]
        P = priority[i][d-1]

        done = False
        # clean()
        for p in P:
            x, y = DIRS[p]

            next_r = r + x
            next_c = c + y
            if 0 <= next_r < N and 0 <= next_c < N:
                si, st = smell[next_r][next_c]
                if si == 0 and st == 0:
                    sharks[i] = p
                    arr[next_r][next_c].append(i)
                    done = True
                    break

        # dirty()
        if not done:
            for p in P:
                x, y = DIRS[p]

                next_r = r + x
                next_c = c + y
                if 0 <= next_r < N and 0 <= next_c < N:
                    si, st = smell[next_r][next_c]
                    if si == i and st > 0:
                        sharks[i] = p
                        arr[next_r][next_c].append(i)
                        done = True
                        break

    # eat() rotten()
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                i = min(arr[r][c])
                arr[r][c].clear()
                arr[r][c].append(i)

            si, st = smell[r][c]
            if st > 0:
                st -= 1

                if st == 0:
                    si = 0
                smell[r][c] = [si, st]

print(answer)
