from collections import deque
from copy import deepcopy

A = []
remains = [5 for _ in range(6)]
remains[0] = 0
for _ in range(10):
    L = list(map(int, input().split()))
    remains[0] += sum(L)
    A.append(L)

answer = -1
queue = deque([[deepcopy(A), deepcopy(remains), 0]])
while queue:
    A, remains, count = queue.pop()
    if remains[0] == 0:
        answer = count
        break

    positions = [deque() for _ in range(6)]
    for r in range(10):
        for c in range(10):
            if A[r][c]:
                for a in range(5, 0, -1):
                    if r + a <= 10 and c + a <= 10:
                        valid = True
                        for x in range(a):
                            for y in range(a):
                                nr = r + x
                                nc = c + y

                                if not A[nr][nc]:
                                    valid = False
                                    break
                            if not valid:
                                break

                        if valid:
                            A[r][c] = a

                            positions[a].append([r, c])
                            break

    for a in range(5, 0, -1):
        Q = positions[a]
        if Q:
            while Q:
                r, c = Q.popleft()

                tempA = deepcopy(A)
                tempRemains = deepcopy(remains)

                if tempA[r][c] == a:
                    for x in range(a):
                        for y in range(a):
                            nr = r + x
                            nc = c + y

                            tempA[nr][nc] = 0
                    tempRemains[a] -= 1
                    tempRemains[0] -= a * a
                    if tempRemains[a] < 0:
                        break
                    else:
                        queue.append([tempA, tempRemains, count + 1])
            break
print(answer)
