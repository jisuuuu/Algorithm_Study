#수들의 합
import sys

s = int(sys.stdin.readline().rstrip())
n = 1

while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1) # 갯수의 최대값을 구하면 되기 때문에 s보다 커질 때 -1