#전투 드로이드 가격
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split())

    print('${:.2f}'.format(a * 350.34  + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90))