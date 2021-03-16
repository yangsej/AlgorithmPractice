import bisect

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    midA = bisect.bisect(A, 0)
    AL = reversed(A[:midA])
    AR = A[midA:]

    midB = bisect.bisect(B, 0)
    BL = reversed(B[:midB])
    BR = B[midB:]

    countL = 0
    for b in BL:
        

    index = 0
    for b in BR:
        for i in range(index, len(AR)):
            if AR[i] <= b:
                index += 1
            else:
                break
        
        for i in range(index, len(AR)):
            
        


    print("@@@@@@@@@@@@@ %i %i @@@@@@@@@@@@@" %(midA, midB))

