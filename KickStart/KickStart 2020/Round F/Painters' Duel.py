def check(museum, RA, PA, RB, PB, AB):
    if RA < 1 or RA >= len(museum) or PA < 1 or PA >= len(museum[RA]) or museum[RA][PA]:
        return None
    else:
        print(RA, PA, RB, PB,  AB)
        museum[RA][PA] = AB

        checks = [0, 0, 0]
        checks[0] = check(museum, RB, PB+1, RA, PA, -AB)

        checks[1] = check(museum, RB, PB-1, RA, PA, -AB)
        
        check_odd = 2 * (PB % 2) - 1
        checks[2] = check(museum, RB + check_odd, PB + check_odd, RA, PA, -AB)

        score = None
        for c in checks:
            if score == None: score = c
            elif c != None: score = max(score, c)
        if score == None:
            checks[0] = check(museum, RA, PA+1, RB, PB, AB)

            checks[1] = check(museum, RA, PA-1, RB, PB, AB)

            check_odd = 2 * (PA % 2) - 1
            checks[2] = check(museum, RA + check_odd, PA + check_odd, RA, PA, -AB)
            
            score = None
            for c in checks:
                if score == None: score = c
                elif c != None: score = max(score, c)
        if score: AB += score
        return AB



T = int(input())
for x in range(T):
    S, RA, PA, RB, PB, C = list(map(int, input().split()))
    museum = [[0 for j in range(2 * i)] for i in range(S+1)]
    museum[RA][PA] = 1

    for i in range(C):
        Ri, Pi = list(map(int, input().split()))
        museum[Ri][Pi] = 2

    answer = 1 + check(museum, RB, PB, RA, PA, -1)
    
    print("Case #%i: %i" %(x+1, answer))
