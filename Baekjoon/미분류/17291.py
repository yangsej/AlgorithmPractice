N = int(input())

counts = [[0, 0, 0, 0, 0], [1, 0, 0, 0]]

for n in range(2, N+1):
    new = 0

    for i in range(2, -1, -1):
        new += counts[1][i]
        counts[1][i+1] = counts[1][i]
        counts[1][i] = 0

    for i in range(3, -1, -1):
        new += counts[0][i]
        counts[0][i+1] = counts[0][i]
        counts[0][i] = 0

    counts[n%2][0] = new

counts[0][4] = 0
counts[1][3] = 0

print(sum(counts[0]) + sum(counts[1]))
