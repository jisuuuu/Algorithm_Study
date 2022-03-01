#가뭄(Small)
import sys
d1, d2, d3 = map(int, sys.stdin.readline().rstrip().split())

a = (d1 + d2 - d3) / 2
b = d1 - a
c = d2 - a

if a <= 0 or b <= 0 or c <= 0:
    print(-1)
else:
    print(1)
    print(a, b, c)