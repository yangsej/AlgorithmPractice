arr = []
for i in range(9):
    arr.append(int(input()))

SUM = sum(arr)
fake = []
for i in range(9):
    s1 = SUM - arr[i]
    for j in range(9):
        if i == j:
            continue
        elif s1 - 100 == arr[j]:
            fake = [i, j]

answers = []
for k in range(9):
    if k not in fake:
        answers.append(arr[k])

answers.sort()
print('\n'.join(map(str, answers)))
