# 별 찍기 - 9
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1))
for i in range(2, n + 1):
    print(' ' * (n - i) + '*' * ((2 * i) - 1))