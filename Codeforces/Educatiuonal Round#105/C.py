import bisect

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in

    midA = bisect.bisect(A, 0)
    AL = reversed(A[:midA])
    AR = A[midA:]

    midB = bisect.bisect(B, 0)
    BL = reversed(B[:midB])
    BR = B[midB:]


    print("@@@@@@@@@@@@@ %i %i @@@@@@@@@@@@@" %(midA, midB))

