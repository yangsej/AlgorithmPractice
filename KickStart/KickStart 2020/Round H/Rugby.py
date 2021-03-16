T = int(input())
for x in range(T):
    N = int(input())
    players = []
    sumX, sumY = 0, 0
    for n in range(N):
        X, Y = map(int, input().split())
        sumX += X
        sumY += Y
        players.append([X,Y])
    players.sort()
    meanX = sumX / N
    meanY = sumY / N

    std_p = -1
    std_d = 10**10
    for i, p in enumerate(players):
        dist = abs(meanX - p[0]) + abs(meanY - p[1])
        if std_d > dist:
            std_d = dist
            std_p = i
        elif std_d == dist:
            if abs(N//2 - std_p) > abs(N//2 - i):
                std_p = i

##    print(std_p, std_d, meanX, meanY)
    answer = 0
    for i, p in enumerate(players):
        dx = abs(players[std_p][0] - p[0] - (std_p - i))
        dy = abs(players[std_p][1] - p[1])
##        print(dx, dy)
        answer += dx + dy


    print("Case #%i: %i" %(x+1, answer))
