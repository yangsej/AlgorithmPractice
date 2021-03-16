N = int(input())
arr = [[0 for i in range(10)] for j in range(N)]
arr[0] = [1 for i in range(10)]
for i in range(1, N):
    for j in range(10):
        arr[i][j] = sum(arr[i-1][j:])
print(sum(arr[N-1])%10007)