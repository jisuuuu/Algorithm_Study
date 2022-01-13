#No Brainer
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if x < y:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')