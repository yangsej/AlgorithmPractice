N = int(input())

arr = [[0, 0] for i in range(N)]
arr[0] = [0, 1]

for i in range(1, N):
    arr[i][0] = sum(arr[i-1])
    arr[i][1] = arr[i-1][0]

print(sum(arr[N-1]))