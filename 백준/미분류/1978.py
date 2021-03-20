import math

N = int(input())
arr = list(map(int, input().split()))
answer = N
for a in arr:
    if a == 1:
        answer -= 1
    else:
        mid = int(math.sqrt(a))
        for i in range(2, mid+1):
            if a % i == 0:
                answer -= 1
                break
print(answer)