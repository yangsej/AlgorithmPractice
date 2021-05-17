from itertools import combinations

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

A = list(combinations(A, M))
A = sorted(list(set(A)))

for a in A:
    print(" ".join(map(str, a)))