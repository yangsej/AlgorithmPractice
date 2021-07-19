from sys import stdin

lines = stdin.readlines()
for line in lines:
    line = input().rstrip()
    tokens = line.split()
    N = len(tokens)
    if N == 0:
        break

    errors = [False] * 6
    errors[5] = True

    hasTwirl = False
    hasHop = False
    DIPs = []
    for i in range(N):
        if tokens[i] == 'twirl':
            hasHop = True
        elif tokens[i] == 'hop':
            hasHop = True
        elif tokens[i] == "dip":
            errors[5] = False
            if not (
                    (i - 1 >= 0 and tokens[i - 1] == "jiggle") or
                    (i - 2 >= 0 and tokens[i - 2] == "jiggle") or
                    (i + 1 < N and tokens[i + 1] == "twirl")
            ):
                errors[1] = True
                tokens[i] = "DIP"

    if N < 3 or not (tokens[-3] == 'clap' and tokens[-2] == 'stomp' and tokens[-1] == 'clap'):
        errors[2] = True

    if hasTwirl:
        if not hasHop:
            errors[3] = True

    if tokens[0] == "jiggle":
        errors[4] = True

    answers = []
    for i in range(1, 6):
        if errors[i]:
            answers.append(str(i))

    M = len(answers)
    answer = "form "
    newline = " ".join(tokens)
    if M == 0:
        answer += "ok: " + newline
    elif M == 1:
        answer += "error %s: %s" %(answers[0], newline)
    else:
        answer += "errors %s and %s: %s" %(', '.join(answers[:M-1]), answers[-1], newline)

    print(answer)
