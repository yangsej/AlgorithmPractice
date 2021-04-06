from collections import deque
N, K = map(int, input().split())

arr = [-1 for i in range(500001)]
queue = deque([N])
bro = deque([K])
answer = 0

arr[N] = 0
while queue:
    n = queue.popleft()

    dif = [n-1, n+1, n*2]
    for d in dif:
        if d >= 0 and d <= 500000 and arr[d] == -1:
            arr[d] = arr[n] + 1
            queue.append(d)

answer = 0
# print(arr)
while K <= 500000:
    # print(answer, K, arr[K])
    if arr[K] == answer: break
    elif arr[K] < answer:
        done = False
        for i in range(answer):
            if K >= 2**i and K%2**i == 0:
                temp = answer - arr[K//2**i] - i
                if temp >= 0 and temp % 2 == 0:
                    done = True
                    break

            if K+i <= 500000:
                temp = answer - arr[K + i] - i
                if temp >= 0 and temp%2 == 0:
                    done = True
                    break
            
            if K-i >= 0:
                temp = answer - arr[K - i] - i
                if temp >= 0 and temp%2 == 0:
                    done = True
                    break
        if done: break
    answer += 1
    K += answer

if K > 500000:
    print(-1)
else:
    print(answer)






# for i, k in enumerate(bro):
#     print(answer + i, k)
#     print(len(queue1))
#     while queue1:
#         n = queue1.popleft()
#         if n == k: break
#         dif = [n-1, n+1, n*2]
#         for d in dif:
#             if arr[d] == -1:
#                 arr[d] = arr[n] + 1
#                 queue2.append(d)

#     if n == k:
#         print(answer + i)
#         break
#     if not queue2 or k > 500000:
#         print(-1)
#         break

#     queue1 = queue2.copy()
#     queue2.clear()