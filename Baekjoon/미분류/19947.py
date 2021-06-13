H, Y = map(int, input().split())

C = [0] * (Y+1)
C[0] = H
for y in range(1, Y+1):
    C[y] = max(C[y], int(C[y-1] * 1.05))
    if y >= 3:
        C[y] = max(C[y], int(C[y-3] * 1.20))
    if y >= 5:
        C[y] = max(C[y], int(C[y-5] * 1.35))
print(int(C[Y]))