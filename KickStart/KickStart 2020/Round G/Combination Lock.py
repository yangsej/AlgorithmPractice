T = int(input())
for x in range(T):
    W, N = map(int, input().split())
    X = list(map(int, input().split()))

    answer = [0, 0]
    s1 = sum(X) // W
    for i in range(len(X)):
        temp = abs(X[i] - s1)
        if temp > N//2:
            temp = N - temp
        answer[0] += temp


    X_temp = X.copy()
    for i in range(len(X)):
        if X_temp[i] < N//2: X_temp[i] += N
    s2 = (sum(X_temp) // W) % N
    if not s2: s2 = N

    for i in range(len(X)):
        temp = abs(X[i] - s2)
        if temp > N//2:
            temp = N - temp
        answer[1] += temp
    answer = min(answer)

    print(s1, s2)
    print("Case #%i: %i" %(x+1, answer))
