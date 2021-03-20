N = int(input())
dp = [[-1 for j in range(10)] for i in range(N+1)]
dp[1] = [1 for i in range(10)]

def solve(n, i):
    if dp[n][i] == -1:
        low = solve(n-1, i-1) if i-1 >= 0 else 0
        high = solve(n-1, i+1) if i+1 < 10 else 0

        dp[n][i] = low + high
    return dp[n][i]
print(sum(solve(N, i) for i in range(1, 10))%1000000000)
# print(dp)
