import math

N, M, K = map(int, input().split())

s = math.comb(N+M, M)
if s < K:
    print(-1)
else:
    answer = ""
    offset = 0
    while N and M:
        s = math.comb(N+M-1, M)

        if K <= offset + s:
            answer += "a"
            N -= 1
        else:
            answer += "z"
            M -= 1
            offset += s

    answer += "a" * N + "z" * M
    print(answer)