import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):

    N, C= map(int, input().split())

    if N * (N+1) // 2 <= C or N-1 > C:
        answer = "IMPOSSIBLE"
    else:
        c = C
        count = [0 for i in range(N+1)]
        for i in range(N, 1, -1):
            if 2 * i - 2 <= c:
                count[i] = i
                c -= i
            elif c <= i-1:
                count[i] = 1
                c -= 1
            else:
                count[i] = c - i + 2
                c = i-2

        answer = [i+1 for i in range(N)]
        for i in range(2, N+1):
            answer = answer[:-count[i]] + list(reversed(answer[-count[i]:]))
        answer = " ".join(map(str, answer))

    

    print("Case #%i: %s" %(t+1, answer))