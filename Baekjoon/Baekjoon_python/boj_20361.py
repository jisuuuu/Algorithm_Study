#일우는 야바위꾼
import sys
n, x, k = map(int, sys.stdin.readline().rstrip().split())
cups = [0 for _ in range(n)]
cups[x - 1] = 1

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a == x or b == x:
        cups[a - 1], cups[b - 1] = cups[b - 1], cups[a - 1]
        x = cups.index(1) + 1
print(x)