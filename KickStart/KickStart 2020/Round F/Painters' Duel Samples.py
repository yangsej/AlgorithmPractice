from itertools import combinations, permutations
nodes = []
S = 2
for i in range(S):
    for j in range(2 * (i+1) - 1):
        nodes.append([i+1, j+1])

print(60)
for i in list(combinations(nodes, 2)):
    for [ra, pa], [rb, pb] in list(permutations(i)):
        print(S, ra, pa, rb, pb, 0)
for i in list(combinations(nodes, 3)):
    for [ra, pa], [rb, pb], [r0, p0] in list(permutations(i)):
        print(S, ra, pa, rb, pb, 1)
        print(r0, p0)
for i in list(combinations(nodes, 4)):
    for [ra, pa], [rb, pb], [r0, p0], [r1, p1] in list(permutations(i)):
        print(S, ra, pa, rb, pb, 2)
        print(r0, p0)
        print(r1, p1)
