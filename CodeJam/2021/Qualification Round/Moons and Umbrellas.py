import sys
input = sys.stdin.readline
from collections import deque


T = int(input())
for t in range(T):
    answer = 0

    X, Y, S = input().split()
    X = int(X)
    Y = int(Y)
    N = len(S)

    # i = 0
    # ???
    # C??
    # J??
    # CC?
    # CJ?
    # JC?
    # JJ?
    # while i < N:
    #     if S[i] == 'C':
    #         if S[i+2] == '?':


    #     if S[i] == S[i+2] and S[i] != '?':
    #     elif S[i] != S[i+2]:
    #         if S[i] != 'C':
    #             if S[i+2] != '?':
    #                 answer += X
    #         elif S[i] != 'J' and S[i+2] != 'C':
    #             answer += Y
    #     i += 2

    #     print(S)


    for i in range(N-1):
        if S[i] == 'C' and S[i+1] == 'J':
                answer += X
        elif S[i] == 'J' and S[i+1] == 'C':
                answer += Y

    print("Case #%i: %i" %(t+1, answer))