T = int(input())
for x in range(T):
    string = input()
    answer = 0
    list_k = []
    list_s = []
    
    index_k = -3
    index_s = -5
    
    while True:
        index_k = string.find("KICK", index_k+3)
        if index_k >= 0: list_k.append(index_k)
        else: break

    while True:
        index_s = string.find("START", index_s+5)
        if index_s >= 0: list_s.append(index_s)
        else: break

    count_k = 0
    for s in list_s:
        if count_k < len(list_k):
            k = list_k[count_k]
            while k < s and count_k < len(list_k):
                count_k += 1
                if count_k == len(list_k): break
                k = list_k[count_k]
        answer += count_k
    print("Case #%i: %i" %(x+1, answer))
