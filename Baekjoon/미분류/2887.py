from sys import stdin
input = stdin.readline

N = int(input())
MAX = 10**10
Nodes = []
for n in range(N):
    x, y, z = list(map(int, input().rstrip().split()))
    Nodes.append((x, y, z, n))

Edges = [[] for _ in range(N)]
for d in range(3):
    Nodes.sort(key=lambda x: x[d])
    for n in range(N-1):
        i = Nodes[n]
        j = Nodes[n+1]
        Edges[i[3]].append((abs(i[d] - j[d]), j[3]))
        Edges[j[3]].append((abs(i[d] - j[d]), i[3]))

for E in Edges:
    E.sort()

Selected = set([0])
Waiting = set([i for i in range(N)])
Waiting.remove(0)
answer = 0
while Waiting:
    md = MAX
    mi = -1
    for node in Selected:
        for d, i in Edges[node]:
            if i in Waiting:
                if d < md:
                    md = d
                    mi = i
                    break
    Waiting.remove(mi)
    Selected.add(mi)
    answer += md

print(answer)