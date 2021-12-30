#명장 남정훈
import sys
l, r, a = map(int, sys.stdin.readline().rstrip().split())
n_min, n_max = min(l, r), max(l, r)
t = min(a, n_max - n_min)

n_min += t
a -= t

result = n_min * 2 + (a // 2 * 2 if a else 0)
print(result)