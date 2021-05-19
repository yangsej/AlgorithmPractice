L = list(map(int, input().split()))

count = 0
answer = 1
for l in L:
    if l % 2 == 1:
        count += 1
        answer *= l

if not count:
    for l in L:
        answer *= l

print(answer)