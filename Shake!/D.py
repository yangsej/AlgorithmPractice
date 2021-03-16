import sys
N, M = map(int,input().split())



edges = []
for m in range(M):
    A, B, L, K = map(int,input().split())
    edges.append([A,B,L,K])


#...
pos = 1
speed = 1
times = [sys.maxsize for i in range(N+1)]
times[pos] = 0
for A, B, L, K in edges:
    if A == pos:
        if speed < K:
            times[B] = L/(speed+1)
        elif speed <= K+1:
            times[B] = L/K
    elif B == pos:
        if speed < K:
            times[A] = L/(speed+1)
        elif speed <= K+1:
            times[A] = L/K

print(times)
#...

