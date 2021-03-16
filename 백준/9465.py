import copy

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]
    
    answer = 0
    temp = copy.deepcopy(arr)
    for i in range(N):
        temp[0][i] -= (arr[0][i-1] if i > 0 else 0) + (arr[0][i+1]  if i < N-1 else 0) + arr[1][i]
        temp[1][i] -= (arr[1][i-1] if i > 0 else 0) + (arr[1][i+1]  if i < N-1 else 0) + arr[0][i]
    
    print(temp)