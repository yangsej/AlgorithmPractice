from collections import deque

T = int(input())
for t in range(T):
    S, E = input().split()

    answer = "IMPOSSIBLE"
    visit = set()
    visit.add(S)
    queue = deque([[S, 0]])
    while queue:
        value, count = queue.popleft()

        if value == E:
            answer = count
            break
        else:
            count += 1

            double = value + "0"
            if double not in visit:
                if len(double) <= 200:
                    visit.add(double)
                    queue.append([double, count])

            neg = ""
            for c in value:
                if c == '0':
                    neg += '1'
                else:
                    neg += '0'
            neg = str(int(neg))

            if neg not in visit:
                visit.add(neg)
                queue.append([neg, count])

    print("Case #%i: %s" %(t+1, answer))
