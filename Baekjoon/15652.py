N, M = map(int, input().split())

arr = []


def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if len(arr) > 0:
            if (i+1) < arr[-1]:
                continue

        arr.append(i + 1)
        dfs()

        arr.pop()


dfs()
