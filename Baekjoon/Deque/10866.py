import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    queue = deque()
    answer = []
    for n in range(N):
        op = input()
        if op.startswith("push_front"):
            queue.appendleft(int(op[11:]))
        elif op.startswith("push_back"):
            queue.append(int(op[10:]))
        elif op.startswith("pop_front"):
            answer.append(queue.popleft() if queue else -1)
        elif op.startswith("pop_back"):
            answer.append(queue.pop() if queue else -1)
        elif op.startswith("size"):
            answer.append(len(queue))
        elif op.startswith("empty"):
            answer.append(0 if queue else 1)
        elif op.startswith("front"):
            answer.append(queue[0] if queue else -1)
        elif op.startswith("back"):
            answer.append(queue[-1] if queue else -1)
    return answer

if __name__ == "__main__":
    answer = solve()
    print("\n".join(map(str, answer)))