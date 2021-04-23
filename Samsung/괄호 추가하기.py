from collections import deque

N = int(input())
F = input()

operators = deque()
operands = deque()

cur = int(F[0])
stack = [[0, cur]]
answer = -2**32
while stack:
    i, cur = stack.pop()

    if i >= N - 1:
        answer = max(answer, cur)
        continue

    i += 1
    operator = F[i]
    i += 1
    operand = int(F[i])

    if operator == '+':
        stack.append([i, cur + operand])
    elif operator == '-':
        stack.append([i, cur - operand])
    elif operator == '*':
        stack.append([i, cur * operand])

    if i < N - 2:
        i += 1
        operator2 = F[i]
        i += 1
        operand2 = int(F[i])

        temp = 0
        if operator2 == '+':
            temp = operand + operand2
        elif operator2 == '-':
            temp = operand - operand2
        elif operator2 == '*':
            temp = operand * operand2

        if operator == '+':
            stack.append([i, cur + temp])
        elif operator == '-':
            stack.append([i, cur - temp])
        elif operator == '*':
            stack.append([i, cur * temp])
print(answer)