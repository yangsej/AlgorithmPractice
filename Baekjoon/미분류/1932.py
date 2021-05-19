from sys import stdin
input = stdin.readline

N = int(input())

A = []
for n in range(N):
    A.append(list(map(int, input().split())))

for n in range(1, N):
    A[n][0] += A[n-1][0]
    A[n][n] += A[n-1][n-1]
    for m in range(1, n):
        A[n][m] += min(A[n-1][m-1], A[n-1][m])
print(max(A[n]))