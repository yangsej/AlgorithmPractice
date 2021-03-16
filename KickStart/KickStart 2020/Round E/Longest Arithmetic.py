from math import ceil

T = int(input())
for x in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    answer = 0
    pre = A[0] - A[1]
    count = 2
    for i in range(1, N-1):
        dif = A[i] - A[i+1]
        if pre == dif:
            count += 1
        else:
            pre = dif
            answer = max(answer, count)
            count = 2
    answer = max(answer, count)
        
        
    print("Case #%i: %s" %(x+1, answer))
