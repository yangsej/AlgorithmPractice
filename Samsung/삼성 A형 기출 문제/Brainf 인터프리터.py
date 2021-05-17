from collections import deque

MAX = 2 ** 8
T = int(input())
for t in range(T):
    answer = "Terminates"
    sm, sc, si = map(int, input().split())
    C = input()
    I = input()

    M = [0 for _ in range(sm)]
    mi = 0
    ci = 0
    ii = 0

    commands = 0

    Loops = deque()
    while ci < sc:
        if commands >= 50000000:
            start = Loops[-1]
            depth = len(Loops) - 1
            while depth < len(Loops):
                c = C[ci]

                if c == '[':
                    Loops.append(ci)
                elif c == ']':
                    Loops.pop()

                ci += 1

            end = ci-1
            answer = "Loops %i %i" %(start, end)
            break

        c = C[ci]

        if c == '-':
            M[mi] -= 1
            if M[mi] == -1:
                M[mi] = MAX - 1
        elif c == '+':
            M[mi] += 1
            if M[mi] == MAX:
                M[mi] = 0
        elif c == '<':
            mi -= 1
            if mi == -1:
                mi = sm - 1
        elif c == '>':
            mi += 1
            if mi == sm:
                mi = 0
        elif c == '[':
            if M[mi] == 0:
                depth = len(Loops)
                Loops.append(ci)
                while depth < len(Loops):
                    ci += 1
                    c = C[ci]

                    if c == '[':
                        Loops.append(ci)
                    elif c == ']':
                        Loops.pop()
            else:
                Loops.append(ci)
        elif c == ']':
            if M[mi] != 0:
                ci = Loops[-1]
            else:
                Loops.pop()
        elif c == '.':
            pass
        elif c == ',':
            if ii < si:
                M[mi] = ord(I[ii])
                ii += 1
            else:
                M[mi] = 255
        ci += 1
        commands += 1
    print(answer)