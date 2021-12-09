#추론
import sys
n = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
result = nums[-1]

if nums[1] - nums[0] == nums[2] - nums[1]:
    result += (nums[1] - nums[0])
elif nums[1] // nums[0] == nums[2] // nums[1]:
    result *= (nums[1] // nums[0])

print(result)