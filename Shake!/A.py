N, T, P = map(int,input().split())
seats = [0 for i in range(N+1)]

seq = [1]
if N > 1:
    seq[1] = N
    dist = 0
    index = 0
    for i in range(2, N):
        seq.append((lo+hi)//2)
        seq.sort()


        for j, lo, hi in enumerate(stack):
            if (hi - lo) > dist:
                index = j
                dist = hi - lo
        lo, hi = stack[index]
        
        if hi - lo >= 3:
            lo = (lo+hi)//2
            seq[i] = lo
        else:
            break




start = [[0, 0] for i in range(T+1)]
end = [[0, 0] for i in range(T+1)]
for t in range(1, T+1):
    s, e = input().split()
    s = int(s[:2]) * 60 + int(s[2:])
    e = int(e[:2]) * 60 + int(e[2:])
    start[t][0] = s
    end[t][0] = e
    start[t][1] = t
    end[t][1] = t
start.sort()
end.sort()
print(start)
print(end)

answer = 0
time = 540
s = 1
e = 1

while time < 1260:
    if time < start[s]:
        time = start[s]
        if sum(seats) == 0:
            answer += start[s] - time
    # elif time == start[s]:

    
    seats[0] = start[s]
    s += 1
    



print()