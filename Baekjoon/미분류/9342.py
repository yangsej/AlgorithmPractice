T = int(input())
for t in range(T):
    S = input()

    answer = "Infected!"
    checks = ['A', 'B', 'C', 'D', 'E', 'F']
    pre = ''
    if S[0] not in checks or S[-1] not in checks:
        answer = "Good"
    else:
        checks = ['A', 'F', 'C']
        index = 0
        pre = 'A'
        for s in S[1:-1]:
            if pre != s:
                index += 1
                if checks[index] != s:
                    answer = "Good"
                    break
            pre = s

    print(answer)