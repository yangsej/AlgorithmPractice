A = '0' + input()
B = '0' + input()

LA = len(A)
LB = len(B)

answer = 0
C = [[0] * (LB+1) for _ in range(LA+1)]
for i in range(1, LA):
    for j in range(1, LB):
        if A[i] == B[j]:
            C[i][j] = C[i-1][j-1] + 1
            if answer < C[i][j]:
                answer = C[i][j]
print(answer)