import sys
N, M, K = map(int,input().split())

queue = []
for n in range(N):
    c, m, p = map(int,input().split())
    queue.append([p, -c, -m, n])

# answer = 0
# for p, c, m in queue:
#     M += c
#     K += m
#     answer += p
#     if M <= 0 and K <= 0:
#         break
# print(answer)


answer = 0
deleted = []

if M > 0 and K > 0:
    queue.sort(key=lambda x: (x[1]+x[2])/x[0])
    while M > 0 and K > 0:
        for p, c, m, i in queue:
            if i not in deleted:
                M += c
                K += m
                answer += p

                deleted.append(i)

if M > 0:
    queue.sort(key=lambda x: x[1]/x[0])
    while M > 0:
        for p, c, m, i in queue:
            if i not in deleted:
                M += c
                K += m
                answer += p

                deleted.append(i)
elif K > 0:
    queue.sort(key=lambda x: x[2]/x[0])
    while K > 0:
        for p, c, m, i in queue:
            if i not in deleted:
                M += c
                K += m
                answer += p

                deleted.append(i)
print(answer)