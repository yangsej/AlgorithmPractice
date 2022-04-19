N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

arr = []
visit = [False] * N


def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if visit[i]: continue
        visit[i] = True

        arr.append(A[i])
        dfs()

        arr.pop()

        visit[i] = False


dfs()
