# 더하기 4
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    print(sum(nums))