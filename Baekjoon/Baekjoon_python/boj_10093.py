#숫자
import sys
a, b = map(int, sys.stdin.readline().split())

if a != b:
    if a > b:
        a, b = b, a
    print(b - a - 1)
    print(*range(a + 1, b))
else:
    print(0)