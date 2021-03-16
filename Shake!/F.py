import sys
import copy
N, M, K = map(int,input().split())

A = [[0, 0] for i in range(N)]
B = [[0, 0] for i in range(M)]
S = [[0, 0] for i in range(K)]

V = list(map(int,input().split()))
minAx, minAy, minAi = 0, sys.maxsize, 0
for i in range(N):
    A[i] = [V[2 * i], V[2 * i + 1]]
    if A[i][1] < minAy:
        minAx = A[i][0]
        minAy = A[i][1]
        minAi = i

V = list(map(int,input().split()))
minBx, minBy, minBi = 0, sys.maxsize, 0
for i in range(M):
    B[i] = [V[2 * i], V[2 * i + 1]]
    if B[i][1] < minBy:
        minBx = B[i][0]
        minBy = B[i][1]
        minBi = i

V = list(map(int,input().split()))
minSx, minSy, minSi = 0, sys.maxsize, 0
for i in range(K):
    S[i] = [V[2 * i], V[2 * i + 1]]
    if S[i][1] < minSy:
        minSx = S[i][0]
        minSy = S[i][1]
        minSi = i

answer = 0

for i in range(N):
    A[i][0] -= minAx
    A[i][1] -= minAy
A.pop(minAi)

A.sort(key=lambda x: x[0]/x[1] if x[1] > 0 else x[0], reverse=True)
A.insert(0, [0, 0])
A.append([0, 0])

AS = copy.deepcopy(S)
for i in range(K):
    AS[i][0] -= minAx
    AS[i][1] -= minAy
    
for n in range(N):
    ax = A[n+1][0] - A[n][0]
    ay = A[n+1][1] - A[n][1]

    for k in range(K):
        sx = AS[k][0] - A[n][0]
        sy = AS[k][1] - A[n][1]

        print(ax*sy - ay*sx)
        if (ax*sy - ay*sx) < 0:
            answer += 1
            break

print("=================")

for i in range(M):
    S[i][0] -= minSx
    S[i][1] -= minSy
S.pop(minSi)

S.sort(key=lambda x: x[0]/x[1] if x[1] > 0 else x[0], reverse=True)
S.insert(0, [0, 0])
S.append([0, 0])

for i in range(M):
    B[i][0] -= minSx
    B[i][1] -= minSy

for k in range(K):
    sx = S[k+1][0] - S[k][0]
    sy = S[k+1][1] - S[k][1]

    for m in range(M):
        bx = B[m][0] - S[k][0]
        by = B[m][1] - S[k][1]

        print(sx*by - sy*bx)
        if (sx*by - sy*bx) < 0:
            answer += 1
            break

if answer == 0:
    print("YES")
else:
    print(answer)