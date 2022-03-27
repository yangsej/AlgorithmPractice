N, M = map(int, input().split())

arr = []
visit = [False] * N


def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(0 if not arr else (arr[-1]), N):
        if visit[i]: continue
        visit[i] = True

        arr.append(i + 1)
        dfs()

        arr.pop()
        visit[i] = False


dfs()

# stack = [[[0] * M, [False] * N, 0]]
#
# while stack:
#     arr, visit, depth = stack.pop()
#
#     if depth == M:
#         print(' '.join(map(str, arr)))
#         continue
#
#     else:
#         for i in range(N, 0, -1):
#             narr = deepcopy(arr)
#             nvisit = deepcopy(visit)
#             if not nvisit[i-1]:
#                 nvisit[i-1] = True
#
#                 narr[depth] = i
#                 stack.append([narr, nvisit, depth + 1])
