#지능형 기차 2
import sys
nums = [-1 for _ in range(10)]
total = 0

for i in range(10):
    off, on = map(int, sys.stdin.readline().rstrip().split())

    total -= off
    total += on

    nums[i] = total

print(max(nums))