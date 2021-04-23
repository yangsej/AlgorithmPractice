from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))

count = 0
R = deque([False for n in range(N)])
answer = 0
while count < K:
    A.appendleft(A.pop())
    R.appendleft(R.pop())
    if R[-1]:
        R[-1] = False

    for i in range(N-1, 0, -1):
        if R[i-1] and not R[i] and A[i] >= 1:
            R[i-1] = False
            R[i] = True
            A[i] -= 1
            if A[i] == 0:
                count += 1
    if not R[0] and A[0] >= 1:
        R[0] = True
        A[0] -= 1
        if A[0] == 0:
            count += 1
    if R[-1]:
        R[-1] = False

    answer += 1
print(answer)