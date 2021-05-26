#수들의 합2
#투포인터 알고리즘

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 0, 0
tot, cnt = 0, 0

while True:
    if tot >= m:
        tot -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        tot += arr[end]
        end += 1

    if tot == m:
        cnt += 1

print(cnt)