import sys
input = sys.stdin.readline
# from collections import deque

def solve():
    N = int(input())
    index = 1
    # stack = deque()
    # answer = deque()
    stack = []
    answer = []
    for n in range(N):
        i = int(input())

        for j in range(index, i+1):
            stack.append(j)
            index += 1
            answer.append("+\n")
        answer.append("-\n")
        top = stack.pop()
        if i != top:
            return "NO"
    return answer

if __name__ == "__main__":
    answer = solve()
    print("".join(answer))