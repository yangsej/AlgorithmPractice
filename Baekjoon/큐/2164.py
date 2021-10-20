import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())
    queue = deque(i+1 for i in range(N))
    for n in range(N-1):
        queue.popleft()
        queue.append(queue.popleft())
    answer = queue[-1]
        
    return answer

if __name__ == "__main__":
    answer = solve()
    print(answer)