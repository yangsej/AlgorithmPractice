T = int(input())

for t in range(T):
    print("Case #%d:" %(t+1))

    R, C = map(int, input().split())

    A = [['.'] * (C * 2 + 1) for _ in range(R * 2 + 1)]

    for r in range(R):
        for c in range(C):
            if r == 0 and c == 0: continue

            A[2*r][2*c] = '+'
            A[2*r][2*c+1] = '-'
            A[2*r][2*c+2] = '+'
            A[2*r+1][2*c] = '|'
            A[2*r+1][2*c+2] = '|'
            A[2*r+2][2*c] = '+'
            A[2*r+2][2*c+1] = '-'
            A[2*r+2][2*c+2] = '+'

    for a in A:
        print(''.join(a))
