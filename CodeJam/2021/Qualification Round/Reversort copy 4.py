import sys
input = sys.stdin.readline
from collections import deque


T = int(input())
for t in range(T):
    answer = 0
    N = int(input())
    L = list(map(int, input().split()))

    

    print("Case #%i: %i" %(t+1, answer))