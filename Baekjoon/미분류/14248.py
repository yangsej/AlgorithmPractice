from collections import deque

N = int(input())
A = list(map(int, input().split()))
S = int(input()) - 1

V = [False] * N
V[S] = True
queue = deque([S])
answer = 1
while queue:
    v = queue.popleft()

    left = v - A[v]
    if left >= 0 and not V[left]:
        V[left] = True
        queue.append(left)
        answer += 1

    right = v + A[v]
    if right < N and not V[right]:
        V[right] = True
        queue.append(right)
        answer += 1
print(answer)