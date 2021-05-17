N = int(input())
A = list(map(int, input().split()))

result = A.pop()
dp = [[0 for _ in range(21)] for _ in range(N-1)]
dp[0][A[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        pre = dp[i-1][j]
        if pre:
            a = A[i]
            p = j + a
            if p <= 20:
                dp[i][p] += pre

            m = j - a
            if m >= 0:
                dp[i][m] += pre

print(dp[N-2][result])
