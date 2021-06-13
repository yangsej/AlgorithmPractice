from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, n):
        self.root = self
        self.count = 1
        self.n = n

    def __repr__(self):
        return " ".join(map(str, [self.n, self.count, "=>", self.root.n]))


N, M, Q = map(int, input().split())
Edges = [[0, 0, False]]
for m in range(M):
    X, Y = map(int, input().split())
    Edges.append([X, Y, True])

A = []
for q in range(Q):
    a = int(input())
    A.append(a)
    Edges[a][2] = False

Union = [Node(n) for n in range(N+1)]
for x, y, v in Edges:
    if v:
        L = []
        x = Union[x]
        while x != x.root:
            L.append(x)
            x = x.root

        y = Union[y]
        while y != y.root:
            L.append(y)
            y = y.root
        L.append(y)

        for l in L:
            l.root = x

for u in Union:
    if u != u.root:
        u.root.count += 1

answer = 0
for a in reversed(A):
    X, Y, V = Edges[a]

    X = Union[X]
    Y = Union[Y]
    L = [X, Y]
    while X != X.root:
        L.append(X)
        X = X.root

    while Y != Y.root:
        L.append(Y)
        Y = Y.root
    L.append(Y)

    if X != Y:
        answer += X.count * Y.count

    for l in L:
        # l.count -= 1
        # counts[X] += 1
        l.root = X

print(answer)