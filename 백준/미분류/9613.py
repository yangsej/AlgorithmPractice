T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    N = arr.pop(0)

    answer = 0
    for i in range(N-1):
        for j in range(i+1, N):
            a = arr[i]
            b = arr[j]
            rem = a
            while rem != 0:
                a = b
                b = rem

                rem = a%b

            answer += b
    print(answer)