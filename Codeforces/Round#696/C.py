from bisect import bisect
T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    queue = []
    first = A.pop()
    target = first
    second = 0
    n = 0
    while n < N-1:
        n += 1
        top = A.pop()
        index = bisect(A, target-top) - 1
        print(A, target, top, target-top, index)
        if index > 0 and A[index] == (target-top):
            queue.append([A.pop(index), top])
        else:
            if second == 0 and queue:
                print(queue)
                n -= 1
                if n < 0:
                    break
                f, s = queue.pop()
                second = s
                A.insert(bisect(A, f), f)
                target = queue[-1][1]
                continue
            else:
                break
        target = top

    if len(A) > 1:
        print("NO")
    else:
        print("YES")
        if second == 0:
            second = A[0]
        print(first + second)
        print(second, first)
        for s, e in queue:
            print(s, e)
    