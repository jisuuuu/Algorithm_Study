#별 찍기 - 17
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    if i == 1 or i == n:
        print(' ' * (n - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')