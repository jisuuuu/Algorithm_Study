#별 찍기 - 12
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * i)
for i in range(n - 1, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * i)