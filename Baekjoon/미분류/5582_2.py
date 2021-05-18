from time import time

start = time()
C = [[0] * 4001 for _ in range(4001)]
print(time() - start)

start = time()
C = [[0 for _ in range(4001)] for _ in range(4001)]
print(time() - start)