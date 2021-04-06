import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    queue = deque()
    answer = []
    for n in range(N):
        op = input()
        if op.startswith("push"):
            queue.append(int(op[5:]))
        elif op.startswith("pop"):
            if queue: answer.append(queue.popleft())
            else: answer.append(-1)
        elif op.startswith("size"):
            answer.append(len(queue))
        elif op.startswith("empty"):
            answer.append(0 if queue else 1)
        elif op.startswith("front"):
            if queue: answer.append(queue[0])
            else: answer.append(-1)
        elif op.startswith("back"):
            if queue: answer.append(queue[-1])
            else: answer.append(-1)
    return answer

if __name__ == "__main__":
    answer = solve()
    print("\n".join(map(str, answer)))