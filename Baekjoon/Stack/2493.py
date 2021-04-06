import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    arr = [[i+1, n] for i, n in enumerate(map(int, input().split()))]
    stack = deque([arr[0]])
    answer = deque([0])

    for n in range(1, N):
        while stack:
            i, top = stack[-1]
            if top > arr[n][1]:
                answer.append(i)
                break
            stack.pop()
        if not stack: answer.append(0)
        stack.append(arr[n])

    return answer

if __name__ == "__main__":
    answer = solve()
    print(" ".join(map(str, answer)))