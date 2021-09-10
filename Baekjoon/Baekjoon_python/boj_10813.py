#공 바꾸기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [i for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    basket[j], basket[i] = basket[i], basket[j]
print(' '.join(list(map(str, basket[1:]))))