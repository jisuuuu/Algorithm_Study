#시그마
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
n_max = max(a, b)
n_min = min(a, b)

total = (a + b) * (n_max - n_min + 1) / 2
print(int(total))