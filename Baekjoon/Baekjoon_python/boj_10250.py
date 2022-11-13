#ACM 호텔
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    num = n // h + 1
    floor = n % h

    if n % h == 0:
        num = n // h
        floor = h
    print(floor * 100 + num)