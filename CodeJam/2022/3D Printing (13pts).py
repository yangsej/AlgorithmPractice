T = int(input())

for t in range(T):
    A = []
    minA = [1000000, 1000000, 1000000, 1000000]
    for i in range(3):
        c, m, y, k = map(int, input().split())
        # A.append(list())
        minA[0] = min(minA[0], c)
        minA[1] = min(minA[1], m)
        minA[2] = min(minA[2], y)
        minA[3] = min(minA[3], k)

    answer = ["IMPOSSIBLE"]
    if sum(minA) >= 1000000:
        total = 1000000

        answer = [0, 0, 0, 0]
        for i in range(4):
            if total >= minA[i]:
                answer[i] = minA[i]
                total -= minA[i]
            else:
                answer[i] = total
                break

    print("Case #%d: %s" % (t+1, ' '.join(map(str, answer))))

