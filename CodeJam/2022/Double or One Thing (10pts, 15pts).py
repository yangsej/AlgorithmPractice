T = int(input())

for t in range(T):
    answer = ""

    S = input()
    l = len(S)

    answer = S
    count = 0
    for i in range(len(S)):
        NS = answer[:i+1 + count] + answer[i + count] + answer[i+1 + count:]
        if NS < answer:
            answer = NS
            count += 1

    print("Case #%i: %s" %(t+1, answer))