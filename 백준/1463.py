N = int(input())
mem = [N for i in range(N+1)]
mem[1] = 0

def solve(n):
    temp = []
    if n%3 == 0:
        temp.append(solve(n//3))
    if n%2 == 0:
        temp.append(solve(n//2))
    temp.append(solve(n-1))

    mem[n] = min(temp) + 1
    return mem[n]

print(solve(N))

# stack = [N]

# while stack:
#     n = stack[-1]
#     if mem[n] == -1:
#         if n%3 == 0:
#             if mem[n//3] == -1:
#                 stack.append(n//3)
#                 continue
#             else:
#                 mem[n] = mem[n//3] + 1
#                 continue
#         else:
#             temp = []
#             if n%2 == 0:
#                 if mem[n//2] == -1:
#                     stack.append(n//2)
#                     continue
#                 else:
#                     temp.append(mem[n-1])

#             if mem[n-1] == -1:
#                 stack.append(n-1)
#                 continue
#             else:
#                 temp.append(mem[n-1])
        
#             mem[n] = min(temp) + 1
#     else:
#         stack.pop()

# print(mem[N])
