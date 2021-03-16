T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    D = {}
    for a in A:
        D.setdefault(a, 0)
        D[a] += 1
    print(max(D.values()))