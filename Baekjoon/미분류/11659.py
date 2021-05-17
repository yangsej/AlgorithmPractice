from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

SUMS = [0]
for a in A:
    SUMS.append(SUMS[-1] + a)

for m in range(M):
    i, j = map(int, input().split())

    print(SUMS[j] - SUMS[i-1])