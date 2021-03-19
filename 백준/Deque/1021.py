import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N, M = map(int,input().split())
    queue = deque(i+1 for i in range(N))
    index = list(map(int, input().split()))

    answer = 0
    for m in range(M):
        count = 0
        while queue[0] != index[m]:
            queue.rotate(1)
            count += 1
        count = min(count, len(queue) - count)
        answer += count
        queue.popleft()
        
    return answer

if __name__ == "__main__":
    answer = solve()
    print(answer)