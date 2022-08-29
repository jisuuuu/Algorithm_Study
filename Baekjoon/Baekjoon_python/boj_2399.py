#거리의 합
import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
total = 0

for i in range(n):
    for j in range(n):
        total += abs(nums[i] - nums[j])
print(total)