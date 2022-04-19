N = int(input())
H = list(map(int, input().split()))

arrow_counts = [0] * 1000001

for h in H:
    if arrow_counts[h] > 0:
        arrow_counts[h] -= 1
        arrow_counts[h-1] += 1
    else:
        arrow_counts[h-1] += 1

print(sum(arrow_counts))


# counts = [0] * (N+1)
# min_val = 10000000
# l, r = -1, -1

# for h in H:
#     counts[h] += 1

# answer = 0
# max_count = 0
# for i in range(N, 0, -1):
#     if max_count < counts[i]:
#         max_count = counts[i]
#     elif counts[i] - max_count < 0:
#         answer += max_count
#         max_count = 0
#
# print(answer)