import sys
input = sys.stdin.readline
from collections import deque

def solve():
    T = int(input())
    answer = []
    for t in range(T):
        P = input()
        N = int(input())
        X = deque()
        if N:
            arr = input()[1:-2].split(",")
            X.extend(map(int, arr))
        else:
            input()

        try:
            reverse = False
            for p in P:
                if p == "R":
                    reverse = not reverse
                elif p == "D":
                    if not reverse: X.popleft()
                    else: X.pop()
            if not reverse:
                answer.append("[" + ",".join(map(str, X)) + "]")
            else: 
                answer.append("[" + ",".join(map(str, reversed(X))) + "]")
        except:
            answer.append("error")


    return answer

if __name__ == "__main__":
    answer = solve()
    print("\n".join(map(str, answer)))