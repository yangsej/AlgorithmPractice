T = int(input())
for x in range(T):
    N, K, S = map(int, input().split())

    answer = K-1 + min(K-S+N-S+1, 1+N)

    print("Case #%i: %i" %(x+1, answer))
