N, M = map(int, input().split())
arr = [input() for n in range(N)]
visit = [[False for m in range(M)] for n in range(N)]
queue1 = []
queue2 = [[0, 0]]

answer = 1
done = False
while queue2 and [N-1, M-1] not in queue2:
    answer += 1
    queue1.extend(queue2)
    queue2 = []
    while queue1:
        i, j = queue1.pop(0)

        if visit[i][j]: continue
        visit[i][j] = True

        
        if arr[i][j] == "1":
            if i < N-1: queue2.append([i+1, j])
            if j < M-1: queue2.append([i, j+1])
            if i > 0: queue2.append([i-1, j])
            if j > 0: queue2.append([i, j-1])
    
print(answer)