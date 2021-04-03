def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)
import sys

n = int(sys.stdin.readline().rstrip())

print(fac(n))
