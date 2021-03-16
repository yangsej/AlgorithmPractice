N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
M = int(input())

arr = [[] for i in range(N+1)]
for i, n in enumerate(A):
    arr[n].append(i)

##print(arr)

for m in range(M):
##    print("===")
    l, r = map(int, input().split())
    answer = 0
    for i in range(l, r+1):
        if (r-i) < answer:
            break
        
        left = 0
        right = N

        for a in arr[A[i]]:
            if l <= a and a <= r:
                left = a
                break

        for a in reversed(arr[A[i]]):
            if l <= a and a <= r:
                right = a
                break

        answer = max(answer, right-left)
    print(answer)
            
