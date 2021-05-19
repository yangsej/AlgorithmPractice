from collections import deque

T = int(input())
for t in range(T):
    P = input()

    answer = "YES"
    queue = deque([[0, len(P) - 1]])
    while queue and answer == "YES":
        l, r = queue.popleft()
        m = (l + r) // 2

        for i in range(m - l):
            if P[l + i] == P[r - i]:
                answer = "NO"
                break

        if r - l > 2:
            queue.append([l, m-1])
            queue.append([m+1, r])

    print(answer)