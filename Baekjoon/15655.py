N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

arr = []
visit = [False] * N

def dfs(pre):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(pre + 1, N):
        if visit[i]: continue
        visit[i] = True

        arr.append(A[i])
        dfs(i)

        arr.pop()

        visit[i] = False


dfs(-1)
