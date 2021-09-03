#이진수

import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    b_nums = list(format(n, 'b'))
    b_nums.reverse()
    for i, b in enumerate(b_nums):
        if b == '1':
            print(i, end=' ')