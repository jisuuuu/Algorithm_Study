#공
import sys
m = int(sys.stdin.readline().rstrip())
cups = [1, 2, 3]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    xi = cups.index(x)
    yi = cups.index(y)

    cups[xi], cups[yi] = cups[yi], cups[xi]
print(cups[0])