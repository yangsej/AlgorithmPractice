T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    answer = "YES"
    for i in range(4):
        if N == arr[i]:
            arr[i-1] -= 1
            arr[(i+1)%4] -= 1
        elif N == arr[i] + 1:
            if arr[(i+1)%4] > 1:
                arr[(i+1)%4] -= 1
            elif arr[i-1] > 1:
                arr[i-1] -= 1
            elif arr[(i+1)%4] == 1:
                arr[(i+1)%4] -= 1
            elif arr[i-1] == 1:
                arr[i-1] -= 1
            else:
                answer = "NO"
                break
        print(arr)
    
    if min(arr) < 0:
        answer = "NO"
    print(answer)

    # for i in range(1, 5):
    #     arr[i] = arr[0] - arr[i]
    # arr = arr[1:]
    # print(arr)

    # keep = [0, 0, 0, 0]
    # for i in range(4):
    #     if arr[i] == 0:
    #         arr[i-1] -= 1
    #         arr[(i+1)%4] -= 1
    #     elif arr[i] == 1:
    #         if arr[i-1] > 1:
    #             arr[i-1] -= 1
    #         elif arr[i-1] > 1:
    #             arr[(i+1)%4] -= 1
    #         else:
    #             arr[i-1] -= 1
    #             arr[(i+1)%4] -= 1
    #             keep[i] = 1
    # print(arr)
    # print(keep)
    
    # answer = "YES"
    # for i in range(4):
    #     if arr[i] < 0:
    #         if keep[i-1]:
    #             keep[i-1] = 0
    #         elif keep[(i+1)%4]:
    #             keep[(i+1)%4] = 0
    #         else:
    #             answer = "NO"
    #             break
    # if sum(keep) > 0:
    #     answer = "NO"

    # print(answer)

