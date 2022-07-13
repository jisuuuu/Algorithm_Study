#좋은 자동차 번호판
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = sys.stdin.readline().split('-')
    b_cnt = int(b)
    a_cnt = 0

    for i in range(3):
        a_cnt += (ord(a[i]) - 65) * 26 ** (2 - i)

    if abs(a_cnt - b_cnt) <= 100:
        print('nice')
    else:
        print('not nice')