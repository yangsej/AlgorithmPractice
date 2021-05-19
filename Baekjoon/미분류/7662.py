import sys
import heapq
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    K = int(input())
    count = 0
    MAP = {}
    MINQ = []
    MAXQ = []
    for k in range(K):
        op, opd = input().rstrip().split()
        opd = int(opd)

        if op == "I":
            heapq.heappush(MINQ, opd)
            heapq.heappush(MAXQ, -opd)
            MAP[opd] = MAP.get(opd, 0) + 1
            count += 1
        else:
            if count:
                count -= 1
                if opd == 1:
                    m = -heapq.heappop(MAXQ)
                    while MAP.get(m, 0) == 0:
                        m = -heapq.heappop(MAXQ)
                else:
                    m = heapq.heappop(MINQ)
                    while MAP.get(m, 0) == 0:
                        m = heapq.heappop(MINQ)
                MAP[m] -= 1
                if MAP[m] == 0:
                    MAP.pop(m)
            else:
                MINQ = []
                MAXQ = []

    if not count:
        print("EMPTY")
    else:
        MAX = -heapq.heappop(MAXQ)
        while MAP.get(MAX, 0) == 0:
            MAX = -heapq.heappop(MAXQ)

        MIN = heapq.heappop(MINQ)
        while MAP.get(MIN, 0) == 0:
            MIN = heapq.heappop(MINQ)

        print(MAX, MIN)