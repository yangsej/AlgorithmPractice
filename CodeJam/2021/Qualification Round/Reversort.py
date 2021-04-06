import sys
input = sys.stdin.readline
from collections import deque


T = int(input())
for t in range(T):
    answer = 0

    N = int(input())
    L = list(map(int, input().split()))

    for i in range(N-1):
        min_val = N+1
        min_ind = 0
        for j in range(i, N):
            if min_val > L[j]:
                min_val = L[j]
                min_ind = j
        L = L[:i] + list(reversed(L[i:min_ind+1])) + L[min_ind+1:]

        answer += min_ind - i + 1

    print("Case #%i: %i" %(t+1, answer))