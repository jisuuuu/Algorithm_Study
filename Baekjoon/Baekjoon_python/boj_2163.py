#초콜릿 자르기

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

print(n - 1 + (m - 1) * n)