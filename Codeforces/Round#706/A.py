T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    st = input()
    count = N%2
    for i in range(N//2):
        if st[i] == st[-1-i]:
            count += 1
        else:
            break
    if count == 0:
        count = 1

    # print(K, count)
    if K < count:
        print("YES")
    else:
        print("NO")