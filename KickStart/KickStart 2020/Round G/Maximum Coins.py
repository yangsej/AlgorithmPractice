T = int(input())
for x in range(T):
    N = int(input())
    mat = []
    for n in range(N):
        mat.append(list(map(int, input().split())))

    counts_x = [0 for i in range(N)]
    counts_y = [0 for i in range(N)]

    for i in range(N):
        for j in range(i, N):
            counts_x[abs(i-j)] += mat[i][j]
            counts_y[abs(i-j)] += mat[j][i]

    answer = max(max(counts_x), max(counts_y))
    print("Case #%i: %i" %(x+1, answer))
