#SASA 모형을 만들어보자
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
if n // 2 < m // 2:
    print(n // 2)
else:
    print(m // 2)