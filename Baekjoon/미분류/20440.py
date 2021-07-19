from sys import stdin
input = stdin.readline

N = int(input())
E = []
X = []
for _ in range(N):
    e, x = map(int, input().split())
    E.append(e)
    X.append(x)

E.sort()
X.sort()

xi = 0
count = 0
c, l, r = (0, -1, -1)
for n in range(N):
    if E[n] == X[xi]:
        xi += 1
    else:
        while xi < N and E[n] > X[xi]:
            if c == count:
                r = X[xi]
            count -= 1
            xi += 1

        if E[n] < X[xi]:
            count += 1
            if c < count:
                c = count
                l = E[n]
                r = -1


if r < 0:
    r = X[xi]
print(c)
print(l, r)