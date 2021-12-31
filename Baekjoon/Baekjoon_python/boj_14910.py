#오르막
import sys
nums = list(map(int, sys.stdin.readline().rstrip().split()))
i = 0

for j in range(1, len(nums)):
    if nums[i] > nums[j]:
        print('Bad')
        break
    i += 1
else:
    print('Good')