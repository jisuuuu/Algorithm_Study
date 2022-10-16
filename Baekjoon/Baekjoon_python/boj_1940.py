#주몽
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
cnt = 0
left, right = 0, n - 1

while left < right:
    if nums[left] + nums[right] == m:
        cnt += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] < m:
        left += 1
    elif nums[left] + nums[right] > m:
        right -= 1
print(cnt)