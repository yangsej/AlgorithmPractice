import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break
    incomes = [0] * (N + 1)
    answer = 0
    MAX = -10000
    for n in range(N):
        P = int(input())
        incomes[n+1] = max(incomes[n] + P, 0)
        answer = max(incomes[n+1], answer)
        MAX = max(MAX, P)
    if MAX < 0:
        answer = MAX
    print(answer)