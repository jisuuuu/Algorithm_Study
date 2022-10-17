# 수 뒤집기
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = sys.stdin.readline().rstrip()
    reversed_n = n[::-1]

    total = str(int(n) + int(reversed_n))

    if total == total[::-1]:
        print('YES')
    else:
        print('NO')