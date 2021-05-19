N = int(input())

costs = []
for n in range(N):
    costs.append(list(map(int, input().split())))

states = []
for c in input():
    if c == 'Y':
        states.append(True)
    else:
        states.append(False)

P = int(input())

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
