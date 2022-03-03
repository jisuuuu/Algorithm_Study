#킹, 퀸, 룩, 비숍, 나이트, 폰
import sys

k, q, l, b, n, p = map(int, sys.stdin.readline().rstrip().split())
print(1 - k, 1 - q, 2 - l, 2 - b, 2 - n, 8 - p)