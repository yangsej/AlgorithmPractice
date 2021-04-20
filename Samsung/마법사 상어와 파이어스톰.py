import copy
from collections import deque

N, Q = map(int, input().split())
A = []
size = 2 ** N
for i in range(size):
   A.append(list(map(int, input().split())))
L = list(map(int, input().split()))

for q in range(Q):
    sub_size = 2**L[q]
    for i in range(2 ** (N-L[q])):
        sub = copy.deepcopy(A[sub_size * i:sub_size * (i + 1)])
        for j in range(2 ** (N-L[q])):
            for k in range(sub_size):
                for l in range(sub_size):
                    A[sub_size * i + l][sub_size * (j+1) - k - 1] = sub[k][sub_size * j + l]

    queue = deque()
    for i in range(size):
        for j in range(size):
            if A[i][j] > 0:
                count = 0
                if i > 0:
                    count += 1 if A[i-1][j] > 0 else 0
                if i < size-1:
                    count += 1 if A[i+1][j] > 0 else 0
                if j > 0:
                    count += 1 if A[i][j-1] > 0 else 0
                if j < size-1:
                    count += 1 if A[i][j+1] > 0 else 0
                if count < 3:
                    queue.append([i, j])

    while queue:
        i, j = queue.popleft()
        A[i][j] -= 1


answer = 0
for i in range(size):
    answer += sum(A[i])
print(answer)

answer = 0
visit = [[False for i in range(size)] for j in range(size)]
queue = deque()
for i in range(size):
    for j in range(size):
        if not visit[i][j]:
            visit[i][j] = True

            if A[i][j] > 0:
                queue.append([i, j])

                count = 0
                while queue:
                    k, l = queue.popleft()
                    count += 1

                    if k > 0:
                        if not visit[k - 1][l]:
                            visit[k-1][l] = True
                            if A[k - 1][l] > 0:
                                queue.append([k-1, l])
                    if k < size - 1:
                        if not visit[k + 1][l]:
                            visit[k + 1][l] = True
                            if A[k + 1][l] > 0:
                                queue.append([k + 1, l])
                    if l > 0:
                        if not visit[k][l - 1]:
                            visit[k][l - 1] = True
                            if A[k][l - 1] > 0:
                                queue.append([k, l - 1])
                    if l < size - 1:
                        if not visit[k][l + 1]:
                            visit[k][l + 1] = True
                            if A[k][l + 1] > 0:
                                queue.append([k, l + 1])
                answer = max(answer, count)
print(answer)