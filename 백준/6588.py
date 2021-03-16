import math

prime = [False, False, True] + [True, False] * 499999

for i in range(3, 1001, 2):
    mid = int(math.sqrt(i))
    for j in range(2, mid+1):
        if i % j == 0:
            prime[i] = False
            break

    if prime[i] == True:
        for j in range(2, 1000000//i + 1):
            prime[i * j] = False

for t in range(100000):
    N = int(input())
    if N == 0:
        break

    Goldbach = False
    for i in range(3, N, 2):
        if prime[i] and prime[N-i]:
            Goldbach = True
            print("%i = %i + %i" %(N, i, N-i))
            break
    if not Goldbach:
        print("Goldbach's conjecture is wrong.")
