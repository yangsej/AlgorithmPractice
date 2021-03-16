import sys
N, M = map(int,input().split())
C = list(map(int,input().split()))
P = int(input())
items = [False for i in range(N)]
tips = []
for p in range(P):
    a, b, t = map(int,input().split())
    tips.append([a, b, t])


answer = 0
for m in range(M):
    diffs = C.copy()
    for a, b, t in tips:
        if not items[b-1]:
            diffs[b-1] = C[b-1] + t
    for i in range(N):
        if items[i]:
            diffs[i] = sys.maxsize

    for n in range(N):
        diffs[n] = [diffs[n], n]
    diffs.sort()

    diff, index = diffs[0]
    items[index] = True
    answer = max(answer, diff)

print(answer)
