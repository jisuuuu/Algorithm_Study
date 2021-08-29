#별 찍기 - 6
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2 * (n - i) - 1):
        print('*', end='')
    print()