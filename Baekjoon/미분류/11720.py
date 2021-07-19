N = int(input())
S = input()

answer = 0
for n in range(N):
    answer += int(S[n])
print(answer)