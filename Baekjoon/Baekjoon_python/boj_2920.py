#음계
import sys
nums = list(map(int, sys.stdin.readline().rstrip().split()))

if nums == sorted(nums):
    print('ascending')
elif nums == sorted(nums, reverse=True):
    print('descending')
else:
    print('mixed')