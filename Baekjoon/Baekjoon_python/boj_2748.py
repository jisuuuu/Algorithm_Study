#피보나치 수 2
import sys
n = int(sys.stdin.readline().rstrip())
cache = [0, 1]

for i in range(2, n + 1):
    cache.append(cache[i - 1] + cache[i - 2])

print(cache[n])