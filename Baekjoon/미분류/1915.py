from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

answer = 0
A = [[0 for _ in range(M+1)] for _ in range(N+1)]
for r in range(N):
    line = input()
    for c in range(M):
        if line[c] == '1':
            check = min(A[r][c], A[r+1][c], A[r][c+1])
            if check:
                A[r+1][c+1] = check + 1
            else:
                A[r+1][c+1] = 1

            if answer < A[r+1][c+1]:
                answer = A[r+1][c+1]
print(answer ** 2)