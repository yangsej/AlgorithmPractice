import bisect
def solution(scoville, K):
    hasHi = False
    scoville.sort()
    i = bisect.bisect(scoville, K)
    if i == 0: return 0
    elif i < len(scoville)-1: 
        scoville = scoville[:i]
        hasHi = True
    else: pass
        
    answer = 0
    while len(scoville) > 1 and scoville[0] < K:  
        answer += 1
        first = scoville.pop(0)
        second = scoville.pop(0)
        new = first + second * 2
        
        if new < K:
            i = bisect.bisect(scoville, new)
            scoville.insert(i, new)
        else: hasHi = True
    
    if (hasHi and len(scoville) == 0) or scoville[0] >= K: return answer
    else: return -1
