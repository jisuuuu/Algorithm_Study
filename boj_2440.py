#별 찍기 - 3
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n, 0, -1):
    for _ in range(i):
        print('*', end='')
    print()
