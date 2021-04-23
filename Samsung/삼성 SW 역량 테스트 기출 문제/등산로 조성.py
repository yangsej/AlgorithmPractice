from collections import deque
import copy

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []

    max_val = 0
    for n in range(N):
        row = list(map(int, input().split()))
        row_max_val = max(row)
        if max_val < row_max_val:
            max_val = row_max_val
        arr.append(row)

    stack = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                stack.append([i, j, 1, [-1, -1, -1],
                              [[False for m in range(N)] for n in range(N)]]) # [row, col, depth, [r, c, h], visit]

    answer = 0
    while stack:
        row, col, depth, [r, c, h], visit = stack.pop()
        visit[row][col] = True
        # print([row, col], depth, [r, c, h])
        # for v in visit:
        #     print(v)
        answer = max(answer, depth)

        height = arr[row][col]
        if row == r and col == c:
            height = h

        def check(row_delta, col_delta):
            next_row = row + row_delta
            next_col = col + col_delta

            if not visit[next_row][next_col]:
                next_height = arr[next_row][next_col]
                if next_height < height:
                    stack.append([next_row, next_col, depth+1, [r, c, h], copy.deepcopy(visit)])
                    # print([row, col], [next_row, next_col], next_height, height)
                    return True
                elif h == -1 and next_height - height < K:
                    stack.append([next_row, next_col, depth+1, [next_row, next_col, height-1], copy.deepcopy(visit)])
                    # print([row, col], [next_row, next_col], next_height, height)
                    return True
            return False

        found_path = False
        found_path |= check(-1, 0) if row > 0 else False
        found_path |= check(1, 0) if row < N-1 else False
        found_path |= check(0, -1) if col > 0 else False
        found_path |= check(0, 1) if col < N-1 else False

    print("#%i %i" %(test_case, answer))