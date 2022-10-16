#쿠키애호가
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, c = map(int, sys.stdin.readline().rstrip().split())

    if n % c == 0:
        print(n // c)
    else:
        print(n // c + 1)