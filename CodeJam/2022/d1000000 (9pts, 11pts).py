T = int(input())

for t in range(T):
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()

    answer = 0
    for n in range(N):
        if D[n] > answer:
            answer += 1

    print("Case #%d: %d" % (t+1, answer))
