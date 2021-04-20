from copy import deepcopy
from collections import deque

positions = [[0, 0] for i in range(17)]
arr = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        id, d = line[2*j:2*(j+1)]
        positions[id] = [i, j]
        arr[i][j] = [id, d]

directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

answer = arr[0][0][0]
arr[0][0][0] = 0

stack = deque([arr[0][0][1], deepcopy(positions), deepcopy(arr)])
while stack:
    shark_d, positions, arr = stack.pop()
    shark_r, shark_c = positions[0]
    shark_x, shark_y = directions[shark_d]

    for i in range(1, 17):
        r, c = positions[i]
        if r >= 0 and c >= 0:
            id, d = arr[r][c]
            for j in range(8):
                x, y = directions[(d+j) % 8]
                new_r = r+x
                new_c = c+y
                if new_r >= 0 and new_r < 4 and new_c >= 0 and new_c < 4:
                    next_id, next_d = arr[new_r][new_c]
                    if next_id == 0:
                        continue

                    positions[next_id] = [r, c]
                    arr[r][c] = [next_id, next_d]

                    positions[id] = [new_r, new_c]
                    arr[new_r][new_c] = [id, d+j]
                    break

    for i in range(1, 4):
        next_shark_r = shark_r + shark_x * i
        next_shark_c = shark_c + shark_y * i
        if next_shark_r >= 0 and next_shark_r < 4 and next_shark_c >= 0 and next_shark_c < 4:
            next_id, next_d = arr[new_r][new_c]
            if next_id == 0:
                continue

            positions[next_id] = [r, c]
            arr[r][c] = [next_id, next_d]

            positions[id] = [new_r, new_c]
            arr[new_r][new_c] = [id, d+j]
            break