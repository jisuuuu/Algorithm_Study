#별 찍기 - 7
import sys
n = int(sys.stdin.readline().rstrip())
# star = [' ' for _ in range(2 * n - 1)]
# for i in range(n):
#     star[(2 * n - 1) // 2 - i] = '*'
#     star[(2 * n - 1) // 2 + i] = '*'
#     print(''.join(star))
#
# for i in range(n - 1):
#     star[i] = ' '
#     star[2 * n - 2 - i] = ' '
#     print(''.join(star))
# 출력 방식 에러...

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(1, n):
    print(' ' * i + '*' * (2 * (n - i) - 1))