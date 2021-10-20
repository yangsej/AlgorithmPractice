T = int(input())

for t in range(1, T + 1):
    DAY, MONTH, QUARTER, YEAR = map(int, input().split())
    days = list(map(int, input().split()))

    prices = [0] * 12
    for m in range(12):
        day = days[m]

        prices[m] = min(day * DAY, MONTH)

    answer = min(YEAR, sum(prices))

    stack = [[0, 0]]
    while stack:
        index, money = stack.pop()

        if index >= 12:
            answer = min(answer, money)
            continue

        if days[index]:
            stack.append([index + 1, money + prices[index]])
            stack.append([index + 3, money + QUARTER])
        else:
            stack.append([index + 1, money])

    print("#%i %i" % (t, answer))
