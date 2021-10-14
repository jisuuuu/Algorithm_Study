#별 찍기 - 16
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * (i - 1) + '*')