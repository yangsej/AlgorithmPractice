N = int(input())
arr = []
arr.append([0 for n in range(N+4)])
arr.append([0 for n in range(N+4)])
for n in range(N):
    line = list(map(int, input().split()))
    line.insert(0, 0)
    line.insert(0, 0)
    line.append(0)
    line.append(0)
    arr.append(line)
arr.append([0 for n in range(N+4)])
arr.append([0 for n in range(N+4)])

R, C = N//2+2, N//2+2
speed = 0
direction = 0 # L D R U 순으로 0 1 2 3
while R != 2 or C != 2:
    if direction == 0 or direction == 2:
        speed += 1

    for i in range(speed):
        if direction == 0:
            C -= 1
        elif direction == 1:
            R += 1
        elif direction == 2:
            C += 1
        elif direction == 3:
            R -= 1

        sand = arr[R][C]
        arr[R][C] = 0
        div = [sand // 100, sand // 50, sand // 20, sand * 7 // 100, sand // 10]
        alpha = sand - div[0] * 2 - div[1] * 2 - div[2] - div[3] * 2 - div[4] * 2

        if direction == 0:
            arr[R - 1][C + 1] += div[0]
            arr[R + 1][C + 1] += div[0]
            arr[R - 2][C] += div[1]
            arr[R + 2][C] += div[1]
            arr[R][C-2] += div[2]
            arr[R][C-1] += alpha
            arr[R - 1][C] += div[3]
            arr[R + 1][C] += div[3]
            arr[R - 1][C - 1] += div[4]
            arr[R + 1][C - 1] += div[4]
            if R == 2 and C == 2:
                break
        elif direction == 1:
            arr[R - 1][C - 1] += div[0]
            arr[R - 1][C + 1] += div[0]
            arr[R][C-2] += div[1]
            arr[R][C+2] += div[1]
            arr[R+2][C] += div[2]
            arr[R+1][C] += alpha
            arr[R][C-1] += div[3]
            arr[R][C+1] += div[3]
            arr[R + 1][C - 1] += div[4]
            arr[R + 1][C + 1] += div[4]
        elif direction == 2:
            arr[R - 1][C - 1] += div[0]
            arr[R + 1][C - 1] += div[0]
            arr[R - 2][C] += div[1]
            arr[R + 2][C] += div[1]
            arr[R][C + 2] += div[2]
            arr[R][C + 1] += alpha
            arr[R - 1][C] += div[3]
            arr[R + 1][C] += div[3]
            arr[R - 1][C + 1] += div[4]
            arr[R + 1][C + 1] += div[4]
        elif direction == 3:
            arr[R + 1][C - 1] += div[0]
            arr[R + 1][C + 1] += div[0]
            arr[R][C - 2] += div[1]
            arr[R][C + 2] += div[1]
            arr[R - 2][C] += div[2]
            arr[R - 1][C] += alpha
            arr[R][C - 1] += div[3]
            arr[R][C + 1] += div[3]
            arr[R - 1][C - 1] += div[4]
            arr[R - 1][C + 1] += div[4]

    direction = (direction + 1) % 4

answer = sum(arr[0]) + sum(arr[1]) + sum(arr[-1]) + sum(arr[-2])
for i in range(2, N+2):
    answer += sum(arr[i][:2]) + sum(arr[i][-2:])
print(answer)
