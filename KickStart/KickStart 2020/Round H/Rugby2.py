T = int(input())
for x in range(T):
    N = int(input())
    PX = []
    PY = []
    for n in range(N):
        X, Y = map(int, input().split())
        PX.append(X)
        PY.append(Y)
    PX.sort()
    PY.sort()
    
    answer = 0

    for i, X in enumerate(PX):
        answer += abs(PX[N//2] - (N//2-i) - X)
    
    for Y in PY:
        answer += abs(PY[N//2] - Y)
    
    print("Case #%i: %i" %(x+1, answer))
