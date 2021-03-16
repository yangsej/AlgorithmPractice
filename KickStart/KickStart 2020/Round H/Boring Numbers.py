T = int(input())
for x in range(T):
    L, R = input().split()
    
    answer = 0
    
    if len(L) != len(R):
        for i in range(int(L), 10 ** len(L)):
            string = str(i)
            isBoring = True
            for j in range(len(string)):
                if j % 2 == 0: #odd
                    if int(string[j]) % 2 == 0:
                        isBoring = False
                        break
                else: #even
                    if int(string[j]) % 2 == 1:
                        isBoring = False
                        break
            if isBoring:
                answer += 1
        for i in range(len(L)+1, len(R)):
            answer += 5 ** i
        for i in range(10 ** (len(R)-1), int(R)+1):
            string = str(i)
            isBoring = True
            for j in range(len(string)):
                if j % 2 == 0: #odd
                    if int(string[j]) % 2 == 0:
                        isBoring = False
                        break
                else: #even
                    if int(string[j]) % 2 == 1:
                        isBoring = False
                        break
            if isBoring:
                answer += 1
    else:
        for i in range(int(L), int(R)+1):
            string = str(i)
            isBoring = True
            for j in range(len(string)):
                if j % 2 == 0: #odd
                    if int(string[j]) % 2 == 0:
                        isBoring = False
                        break
                else: #even
                    if int(string[j]) % 2 == 1:
                        isBoring = False
                        break
            if isBoring:
                answer += 1
        
    print("Case #%i: %i" %(x+1, answer))
