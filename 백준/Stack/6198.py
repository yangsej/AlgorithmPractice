import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    stack = deque([int(input())])
    answer = 0
    for n in range(1, N):
        h = int(input())
        while stack:
            top = stack[-1]
            if top > h:
                break
            stack.pop()
            answer += len(stack)
        stack.append(h)

    while stack:
        stack.pop()
        answer += len(stack)

    return answer


if __name__ == "__main__":
    answer = solve()
    print(answer)