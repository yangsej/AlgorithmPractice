import math

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    S = set(map(int, input().split()))
    SS = set([])

    print(S)
    mex = 0
    for k in range(K):
        if SS:
            mex = min(SS)
        mex = min(min(S), mex)
        mex = min(SS) if SS else, key=lambda x: (x >= mex and x+1 not in S)) + 1
        new = math.ceil((mex + max(S)) / 2)
        SS.add(new)
        print(mex, new)
    print(S)
