from collections import deque

cmds = list(map(int, input().split()))
N = len(cmds)
MAX = 4 * N
COSTS = [[1, 2, 2, 2, 2],
         [2, 1, 3, 4, 3],
         [2, 3, 1, 3, 4],
         [2, 4, 3, 1, 3],
         [2, 3, 4, 3, 1]]

dp = [[MAX] * 5 for _ in range(N)]
dp[0][0] = 0

for i in range(N-1):
    c = cmds[i]
    d = cmds[i+1]
    value = min(dp[i])

    for j in range(5):
        if value == dp[i][j]:
            s1 = COSTS[c][d]
            s2 = COSTS[j][d]

            if s1 <= s2:
                dp[i+1][j] = min(dp[i+1][j], value + s1)

            if s1 >= s2:
                dp[i+1][c] = min(dp[i+1][j], value + s2)
print(min(dp[N-1]))

# queue = deque([[cmds[0], 0, 1]])
# while queue:
#     l, r, i = queue.popleft()
#     d = cmds[i]
#
#     ls = COSTS[l][d]
#     rs = COSTS[r][d]
#
#     dp[i][l]
#     if not dp[i+1][l]:
#         dp[i+1][l] = ls
#     else:
#         if ls < dp[i][l]:
#             dp[i][l] = ls
#
#
#     if i < N-1:
#         if ls <= rs:
#             dp[i+1] = dp[i] + ls
#             queue.append([d, r, i+1])
#
#         if ls >= rs:
#             dp[i+1] = dp[i] + rs
#             queue.append([l, d, i+1])
# print(dp[N-1])