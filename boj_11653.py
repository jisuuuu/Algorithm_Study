#소인수분해

import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
dic = defaultdict(int)

d = 2 #소수 중 최소 값인 2로 초기화

while d <= n:
    if n % d == 0:
        dic[d] += 1
        n = n / d
    else:
        d += 1

for item in dic.items():
    for _ in range(item[1]):
        print(item[0])