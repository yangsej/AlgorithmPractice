from sys import stdin
input = stdin.readline

N = int(input())
X = []
Y = []
for n in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

x = X[N//2]
y = Y[N//2]

answer = 0
for n in range(N):
    answer += abs(X[n] - x) + abs(Y[n] - y)
print(answer)