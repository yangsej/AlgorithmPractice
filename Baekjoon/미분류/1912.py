N = int(input())
arr = list(map(int, input().split()))

subsum = [0 for i in range(N)]
subsum[0] = arr[0]
for i in range(1, N):
    subsum[i] = subsum[i-1] + arr[i]
    if subsum[i] < 0:
        subsum[i] = 0

result = max(subsum)
if result == 0:
    result = max(arr)
    
print(result)