T = int(input())
for x in range(T):
    answer = 0
    N, K = list(map(int, input().split()))
    deploys = []
    for n in range(N):
        deploys.append(list(map(int, input().split())))
    deploys.sort()

    i = 0
    s = 0
    while i < N:
        if not s:
            s = deploys[i][0]
        e = deploys[i][1]
        inter = e - s

        if inter > K:
            s = e - inter % K
            if s == e:
                s = 0
                i += 1
            answer += inter // K
        elif inter == K:
            s = 0
            i += 1
            answer += 1
        else:
            i += 1
            if i == N:
                answer += 1
                break
            if s + K <= deploys[i][0]:
                s = 0
                answer += 1
    print("Case #%i: %i" %(x+1, answer))

