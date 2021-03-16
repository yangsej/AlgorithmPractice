T = int(input())
for t in range(T):
    N = int(input())
    mem = [0 for i in range(12)]
    mem[1] = 1
    mem[2] = 2
    mem[3] = 4


    def solve(x):
        if mem[x] == 0:
            mem[x] = solve(x-3) + solve(x-2) + solve(x-1)
        return mem[x]
            
    print(solve(N))
