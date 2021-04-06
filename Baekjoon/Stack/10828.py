import sys
input = sys.stdin.readline
from collections import deque
stack = deque()
for n in range(int(input())):
    op = input()
    if op.startswith("push"):
        stack.append(int(op[5:]))
    elif op.startswith("pop"):
        if stack: print(stack.pop())
        else: print(-1)
    elif op.startswith("size"):
        print(len(stack))
    elif op.startswith("empty"):
        print(0 if stack else 1)
    elif op.startswith("top"):
        if stack: print(stack[-1])
        else: print(-1)