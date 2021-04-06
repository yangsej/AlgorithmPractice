N = int(input())
mem = [0 for i in range(1001)]
mem[1] = 1
mem[2] = 2


def fib(x):
    if mem[x] == 0:
        mem[x] = fib(x-2) + fib(x-1)
    return mem[x]
        
print(fib(N)%10007)
