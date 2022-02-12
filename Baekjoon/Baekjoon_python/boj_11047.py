#동전0
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
coin = list()

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

count = 0
for i in reversed(range(n)):
    count += k // coin[i]
    k = k % coin[i]
print(count)