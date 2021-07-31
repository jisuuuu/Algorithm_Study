#과자
import sys
k, n, m = map(int, sys.stdin.readline().rstrip().split())
if k * n - m > 0:
    print(k * n - m)
else:
    print(0)