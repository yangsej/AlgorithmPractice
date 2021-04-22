import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

arr = []
red = [0, 0]
blue = [0, 0]
out = [0, 0]
for n in range(N):
    line = arr.append(input())
    for m in range(M):
        if line[m] == 'R':
            red = [n, m]
            line[m] = '.'
        elif line[m] == 'B':
            blue = [n, m]
            line[m] = '.'
        elif line[m] == 'O':
            out = [n, m]
    arr.append(line)

queue = deque([0, '', red, blue])

answer = 0
while queue:
    count, way, red, blue = queue.popleft()
    if count > 10:
        answer = -1
        break

    vertical = False
    horizontal = False
    if red[1] == blue[1]: # R B 서로 위아래로 존재
        vertical = True
    elif red[0] == blue[0]: # R B 서로 좌우로 존재
        horizontal = True

    # 위
    while arr[red[0]-1][red[1]] != '#' or arr[blue[0]-1][blue[1]] != '#':
        if vertical and red[0] < blue[0]: # R ... B
        else:
            if arr[red[0]-1][red[1]] != '#': red[0] -= 1
            if arr[blue[0]-1][blue[1]] != '#': blue[0] -= 1

        if red[0] - blue[0] == 1:  # B 아래 R

        if red[1] - blue[1] == 1:  # B 오른쪽 R
        if red[1] - blue[1] == -1:  # B 왼쪽 R


print(answer)