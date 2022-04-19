from sys import stdin
from collections import  deque

input = stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for m in range(M):
    a, b, c = list(map(int, input().split()))
    arr[a].append((b, c))
    arr[b].append((a, c))


queue = deque()
queue.append(1)

visit = [1000000000] * (N+1)
visit[1] = 0


while queue:
    node = queue.popleft()

    for b, c in arr[node]:
        if visit[node] + c < visit[b]:
            visit[b] = visit[node] + c

            queue.append(b)

print(visit[N])