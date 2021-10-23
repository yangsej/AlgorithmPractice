from copy import deepcopy

N = int(input())

A = []
for n in range(N):
    A.append(list(map(int, input().split())))

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0
stack = [(0, deepcopy(A))]

while stack:
    count, arr = stack.pop()

    if count == 5:
        for a in arr:
            answer = max(answer, max(a))
        continue
    count += 1

    for d in range(len(DIRS)):
        dr, dc = DIRS[d]
        narr = deepcopy(arr)

        if dc == -1:
            for i in range(N):
                for j in range(N):


        stack.append((count, narr))

