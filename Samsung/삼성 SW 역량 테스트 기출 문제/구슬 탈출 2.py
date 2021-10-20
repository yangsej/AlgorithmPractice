from collections import deque

N, M = map(int, input().split())

DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
red = [0, 0]
blue = [0, 0]

A = [[""] * M for _ in range(N)]
for n in range(N):
    line = input()
    for m in range(M):
        A[n][m] = line[m]
        if A[n][m] == 'R':
            A[n][m] = '.'
            red = [n, m]
        elif A[n][m] == 'B':
            A[n][m] = '.'
            blue = [n, m]

answer = 11
queue = deque([[red, blue, 0, -1]]) # red, blue, count, pre_dir

while queue:
    [rr, rc], [br, bc], count, pd = queue.popleft()

    if count >= 10: continue
    count += 1

    for d in range(len(DIRS)):
        if pd == d: continue
        dr, dc = DIRS[d]

        rout, bout = False, False

        prr, prc = rr, rc
        pbr, pbc = br, bc

        while True:
            nrr, nrc = prr + dr, prc + dc
            nbr, nbc = pbr + dr, pbc + dc

            if A[nrr][nrc] == 'O':
                rout = True
                prr, prc = -1, -1
                nrr, nrc = -1, -1
            if A[nbr][nbc] == 'O':
                bout = True
                break

            if A[nrr][nrc] == '#' or (nrr == pbr and nrc == pbc) or rout:
                nrr, nrc = prr, prc
            if A[nbr][nbc] == '#' or (nbr == prr and nbc == prc) or bout:
                nbr, nbc = pbr, pbc

            if prr == nrr and prc == nrc and pbr == nbr and pbc == nbc: break

            prr, prc = nrr, nrc
            pbr, pbc = nbr, nbc

        if bout: continue
        elif rout:
            answer = count
            queue.clear()
            break

        if rr == prr and rc == prc and br == pbr and bc == pbc: continue

        queue.append([[prr, prc], [pbr, pbc], count, d])

if answer == 11:
    answer = -1

print(answer)
