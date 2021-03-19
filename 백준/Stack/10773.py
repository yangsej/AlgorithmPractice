import sys
input = sys.stdin.readline
from collections import deque

stack = deque()
for k in range(int(input())):
    n = int(input())
    if n: stack.append(n)
    else: stack.pop()

print(sum(stack))