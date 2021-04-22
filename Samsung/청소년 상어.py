from copy import deepcopy
from collections import deque

positions = [[0, 0] for i in range(17)]
arr = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        id, d = line[2 * j:2 * (j + 1)]
        positions[id] = [i, j]
        arr[i][j] = [id, d]

directions = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

answer = 0
id, d = arr[0][0]
arr[0][0][0] = -1
positions[id] = [-1, -1]
stack = deque([[id, arr[0][0][1], positions, arr]])
while stack:
    score, shark_d, positions, arr = stack.pop()
    shark_r, shark_c = positions[0]
    shark_x, shark_y = directions[shark_d]

    for i in range(1, 17):
        r, c = positions[i]
        if r >= 0 and c >= 0:
            id, d = arr[r][c]
            for j in range(8):
                new_d = (d + j - 1) % 8 + 1
                x, y = directions[new_d]
                new_r = r + x
                new_c = c + y
                if 0 <= new_r < 4 and 0 <= new_c < 4:
                    next_id, next_d = arr[new_r][new_c]
                    if next_id == -1:
                        continue

                    positions[next_id] = [r, c]
                    arr[r][c] = [next_id, next_d]

                    positions[id] = [new_r, new_c]
                    arr[new_r][new_c] = [id, new_d]
                    break

    count = 0
    for i in range(1, 4):
        next_shark_r = shark_r + shark_x * i
        next_shark_c = shark_c + shark_y * i
        if 0 <= next_shark_r < 4 and 0 <= next_shark_c < 4:
            next_positions = deepcopy(positions)
            next_arr = deepcopy(arr)
            next_id, next_d = next_arr[next_shark_r][next_shark_c]
            if next_id > 0:
                next_score = score + next_id
            else:
                continue

            next_positions[0] = [next_shark_r, next_shark_c]
            next_positions[next_id] = [-1, -1]
            next_arr[shark_r][shark_c] = [0, 0]
            next_arr[next_shark_r][next_shark_c][0] = -1

            count += 1
            stack.append([
                next_score,
                next_d,
                next_positions,
                next_arr])
        else:
            break
    if count == 0:
        answer = max(answer, score)
print(answer)