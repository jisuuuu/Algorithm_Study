#악마의 제안
import sys
k, n = map(int, sys.stdin.readline().rstrip().split())

if n == 1:
    print(-1)
else:
    tmp = (k * n) // (n - 1)
    if (k * n) % (n - 1):
        tmp += 1
    print(tmp)