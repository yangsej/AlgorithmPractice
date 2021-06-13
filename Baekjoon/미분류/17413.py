S = input()
l = 0
tag = False
answers = []
for i in range(len(S)):
    if S[i] == '<':
        if l < i:
            answers.append(S[l:i])
        l = i
        tag = True
    elif S[i] == '>':
        answers.append(S[l:i+1])
        l = i+1
        tag = False
    elif S[i] == ' ':
        if not tag:
            answers.append(S[l:i])
            answers.append(' ')
            l = i+1
if l < len(S):
    answers.append(S[l:len(S)])

answer = ""
for a in answers:
    if a[0] == '<':
        answer += a
    else:
        answer += a[::-1]
print(answer)