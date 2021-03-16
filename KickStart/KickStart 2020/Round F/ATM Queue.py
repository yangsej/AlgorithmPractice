from math import ceil

T = int(input())
for x in range(T):
    answer = ""
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    A = [[ceil(A[i]/X), i+1] for i in range(len(A))]

    A.sort()
    
    for a, i in A:
        answer += str(i) + " "
        
    print("Case #%i: %s" %(x+1, answer))
