#전북대학교
import sys
n = int(sys.stdin.readline().rstrip())

if n % 2 == 0:
    print('I LOVE CBNU')
else:
    print('*' * n)
    print(' ' * (n // 2) + '*')

    for i in range(n // 2):
        print(' ' * (n // 2 - i - 1) + '*' + ' ' * (i * 2 + 1) + '*')