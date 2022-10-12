#한다 안한다
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a = list(sys.stdin.readline().rstrip())
    k = len(a) // 2 - 1

    if a[k] == a[-k - 1]:
        print('Do-it')
    else:
        print('Do-it-Not')