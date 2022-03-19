#별 찍기 - 21
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    print('* ' * (n - n // 2))
    print(' *' * (n // 2))