#가희와 방어율 무시
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
n = a * (100 - b) / 100
if n >= 100:
    print(0)
else:
    print(1)