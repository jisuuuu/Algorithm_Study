#공 넣기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [0 for _ in range(n + 1)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())

    for r in range(i, j + 1):
        basket[r] = k

print(' '.join(list(map(str, basket[1:]))))