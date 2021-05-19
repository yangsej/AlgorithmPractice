N = int(input())

S = [0] * N
for n in range(N):
    S[n] = int(input())

S1 = [0] * N
for n in range(1, N):
    S1[n] = S[n] + S[n-1]
S2 = [0] * N
for n in range(2, N):
    S2[n] = S[n] + S[n-2]

answer = 0
index = N-1
while index >= 0:
    if S1[n] <= S2[n]:

    index

print(S[N+1])