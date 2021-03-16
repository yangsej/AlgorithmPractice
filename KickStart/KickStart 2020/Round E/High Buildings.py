T = int(input())
for x in range(T):
    N, A, B, C = list(map(int, input().split()))

    Arr = [0 for i in range(N)]

    if N < A+B-C:
        answer = "IMPOSSIBLE"
    else:
        for i in range(N):
            if i < A-C: Arr[i] = i+2
            elif i < A-1: Arr[i] = N
            elif C == 1 and A-1 == i: Arr[i] = N
            elif i <= N-B: Arr[i] = 1
            elif i < N-B+C: Arr[i] = N
            else: Arr[i] = N-i+1
        answer = "".join(map(lambda x: str(x) + " ", Arr))
        
    print("Case #%i: %s" %(x+1, answer))
