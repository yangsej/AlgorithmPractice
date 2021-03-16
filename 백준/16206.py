N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

answer = 0
for a in A:
    if a % 10 == 0:
        answer += a // 10
        M -= a//10 - 1
        if M < 0:
            answer += M - 1
            M = 0
            break

for a in A:
    if a % 10 != 0:
        answer += a // 10
        M -= a//10
        if M < 0:
            answer += M
            break

print(answer)