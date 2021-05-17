from collections import deque
from itertools import permutations
# import time

N = int(input())

innings = []
for n in range(N):
    L = list(map(int, input().split()))
    innings.append(L)


# timesum = 0.0
# timecount = 0

answer = 0
seqs = permutations([i for i in range(1, 9)], 8)
bases = [False for _ in range(4)]
for seq in seqs:
    seq = list(seq)
    seq.insert(3, 0)
    # seq.insert(3, 0)

    index = 0
    score = 0
    for n in range(N):
        for i in [1, 2, 3]:
            bases[i] = False
        out = 0

        while out < 3:
            hit = innings[n][seq[index]]
            index = (index + 1) % 9
            if hit == 0:
                out += 1
            elif hit == 4:
                # start = time.time()
                score += 1
                if bases[3]:
                    score += 1
                    bases[3] = False
                if bases[2]:
                    score += 1
                    bases[2] = False
                if bases[1]:
                    score += 1
                    bases[1] = False
                #
                # duration = time.time() - start
                # if duration > 0.0:
                #     timesum += duration
                #     timecount += 1
            else:
                for i in [3, 2, 1]:
                    if bases[i]:
                        bases[i] = False
                        if i + hit > 3:
                            score += 1
                        else:
                            bases[i+hit] = True
                bases[hit] = True

    if score > answer:
        answer = score
# print(timecount, timesum)
print(answer)