N, M = map(int, input().split())
arr = [[] for n in range(N)]
for n in range(N):
    arr[n] = list(map(int, input().split()))

visit = [[False for m in range(M)] for n in range(N)]
stack = []

answer = [0, 0]
for n in range(N):
    for m in range(M):
        if visit[n][m]: continue

        if arr[n][m]:
            answer[0] += 1
            area = 0
            stack.append([n, m])
            while stack:
                i, j = stack.pop()

                if visit[i][j]: continue
                visit[i][j] = True

                if arr[i][j]:
                    area += 1
                    if i > 0: stack.append([i-1, j])
                    if i < N-1: stack.append([i+1, j])
                    if j > 0: stack.append([i, j-1])
                    if j < M-1: stack.append([i, j+1])
            answer[1] = max(answer[1], area)
        
        visit[n][m] = True

print(answer[0])
print(answer[1])