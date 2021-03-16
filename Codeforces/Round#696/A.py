T = int(input())
for t in range(T):
    N = int(input())
    b = input()
    a = "1"

    for n in range(1, N):
        if (int(a[n-1]) + int(b[n-1])) == int(b[n]) + 1:
            a += "0"
        else:
            a += "1"
    
    print(a)