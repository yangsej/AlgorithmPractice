N = int(input())
P = list(map(int, input().split()))

max_count = 0
max_index = 0
for i in range(N//2, 0, -1):
    m = P[i]
    count = 0
    for j in range(1, i+1):
        l = P[i-1]
        r = P[i+1]
        if not(m > l and m > r):
            break
        else:
            count += 1
    if count > max_count:
        max_count = count
        max_index = i
            
for i in range(N//2, 0, -1):
    m = P[i]
    count = 0
    for j in range(1, i+1):
        l = P[i-1]
        r = P[i+1]
        if not(m > l and m > r):
            break
        else:
            count += 1
    if count > max_count:
        max_count = count
        max_index = i
        