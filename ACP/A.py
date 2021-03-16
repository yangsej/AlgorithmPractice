def main():
    m, Seed, X1, X2 = map(int, input().split())
    for i in range(m):
        temp = m * i + X1
        for a in range(temp // Seed + 1):
            c = temp - a * Seed
            print(a, c)

            if X2 == (a * X1 + c) % m:
                print(a, c)
                return

if __name__ == "__main__":
    main()
