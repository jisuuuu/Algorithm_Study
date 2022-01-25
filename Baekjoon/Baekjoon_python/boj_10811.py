#바구니 뒤집기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())

    basket = basket[:i - 1] + basket[i - 1:j][::-1] + basket[j:]
print(' '.join(list(map(str, basket))))