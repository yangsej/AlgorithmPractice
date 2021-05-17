T = int(input())
for t in range(T):
    Y = input()
    L = len(Y)

    answers = []
    if L > 1:
        for i in range(L//2, 0, -1):
            pre = Y[:i]
            subs = [int(pre)]
            ls = len(str(subs[-1] + 1))
            index = ls
            while index < L:
                ls = len(str(subs[-1] + 1))
                sub = Y[index:index+ls]

                if int(pre) + 1 >= int(sub):
                    subs.append(subs[-1] + 1)
                else:
                    for j in range(len(subs)):
                        subs[-j-1] = int(sub) - j - 1
                    subs.append(int(sub))

                index += ls

            string = "".join(map(str, subs))
            if Y == string:
                for j in range(len(subs)):
                    subs[j] += 1
                string = "".join(map(str, subs))

            answers.append(string)
    else:
        answers.append(Y + str(int(Y)+1))
    answers = map(int, answers)
    answer = min(answers)

    print("Case #%i: %s" %(t+1,  answer))