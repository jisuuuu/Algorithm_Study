#점수 집계
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))

    if max(nums) - min(nums) >= 4:
        print('KIN')
    else:
        print(sum(nums))