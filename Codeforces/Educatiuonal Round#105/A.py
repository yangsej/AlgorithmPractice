N = int(input())
for n in range(N):
    line = input()

    count = {'A' : 0, 'B' : 0, 'C' : 0}
    for c in line:
        count[c] += 1

    first = line[0]
    last = line[-1]

    if first == last:
        print("NO")
    else:
        num = 0
        if count[first] == len(line)//2:
            for c in line:
                if c == first:
                    num += 1
                else:
                    num -= 1
                if num < 0:
                    print("NO")
                    break
            if num == 0: print("YES")
        elif count[last] == len(line)//2:
            for c in line:
                if c == last:
                    num -= 1
                else:
                    num += 1
                if num < 0:
                    print("NO")
                    break
            if num == 0: print("YES")
        else:
            print("NO")
