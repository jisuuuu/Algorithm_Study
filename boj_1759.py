#암호 만들기
import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().rstrip().split())
a = sorted(sys.stdin.readline().rstrip().split())
b = set('aeiou')

com = list(combinations(a, l))

for c in com:
    n = set(c) - b
    if 2 <= len(n) and l - len(n) >= 1:
        print(''.join(c))