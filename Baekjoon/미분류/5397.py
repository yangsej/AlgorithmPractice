from collections import deque

T = int(input())
for t in range(T):
    L = input()

    left = deque()
    right = deque()

    for l in L:
        if l == '<':
            if left:
                right.appendleft(left.pop())
        elif l == '>':
            if right:
                left.append(right.popleft())
        elif l == '-':
            if left:
                left.pop()
        else:
            left.append(l)

    answer = "".join(left + right)

    print(answer)