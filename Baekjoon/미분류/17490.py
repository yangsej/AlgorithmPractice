from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
S = list(map(int, input().split()))
cuts = []
for m in range(M):
    i, j = map(int, input().split())
    cuts.append([i, j])
cuts.sort()


for m in range(M):
    i, j = cuts[m]
    l = cuts[m-1][1]
    r = i

    if l > r:
        r = N+i

    MIN = 1000000
    for k in range(l, r+1):
        index = (k-1+N) % N
        if S[index] < MIN:
            MIN = S[index]
    K -= MIN

    for k in range(i+1, j):
        K -= S[k]

if K < 0:
    print("NO")
else:
    print("YES")