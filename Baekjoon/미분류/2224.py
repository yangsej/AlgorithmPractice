from functools import cmp_to_key

X = int(input())

Props = {}
for _ in range(X):
    P, _, Q = input().split()

    if P != Q:
        Props[P] = Q


Items = sorted(Props.items())
answers = []
for P, Q in Items:
    answers.append((P, Q))
    while Q in Props:
        Q = Props[Q]
        if P == Q:
            break
        else:
            answers.append((P, Q))

ORDER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ORDER += ORDER.lower()
ORDERS = {}

for i in range(len(ORDER)):
    ORDERS[ORDER[i]] = i

answers.sort(key=lambda x: (ORDERS[x[0]], ORDERS[x[1]]))

print(len(answers))
for P, Q in answers:
    print(P + " => " + Q)