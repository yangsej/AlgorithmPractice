import math

T = int(input())
for t in range(T):
    N = int(input())
    miners = []
    mines = []
    answer = 0
    for n in range(N * 2):
        x, y = map(int, input().split())
        if x == 0:
            miners.append(y)
        else:
            mines.append(x)
    miners.sort(key=lambda x: abs(x))
    mines.sort(key=lambda x: abs(x))

    for i in range(N):
        answer += math.sqrt(math.pow(miners[i], 2) + math.pow(mines[i], 2))
    print(answer)

    