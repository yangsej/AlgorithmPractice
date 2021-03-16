T = int(input())
for t in range(T):
    A, B = map(int, input().split())

    a = A
    b = B
    rem = A
    while rem != 0:
        a = b
        b = rem

        rem = a%b

    GCD = b
    print(A*B//GCD)