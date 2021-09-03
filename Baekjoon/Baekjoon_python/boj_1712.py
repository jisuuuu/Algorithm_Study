#손익분기점
import sys

a, b, c = map(int, sys.stdin.readline().split())
if b < c:
    print(int(a // (c - b)) + 1)
else:
    print(-1)