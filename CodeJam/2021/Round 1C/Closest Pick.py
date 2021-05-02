from math import ceil
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    answer = 0.0

    P.sort()

    left = P[0] - 1
    right = K - P[N-1]
    difs = []
    for n in range(1, N):
        dif = P[n] - P[n-1] - 1
        difs.append(dif)
    difs.sort(reverse=True)

    count = left + right
    if difs:
        count = max(count, max(left, right) + ceil(difs[0]/2))
        count = max(count, difs[0])
        if len(difs) >= 2:
            count = max(count, ceil(difs[0]/2) + ceil(difs[1]/2))

    answer = count / K

    print("Case #%i: %f" %(t+1,  answer))
