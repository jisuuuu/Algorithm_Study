#쉽게 푸는 문제
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
nums = []

for i in range(1, 46): #1000번째 수를 대략적으로 구하면 n * (n + 1) / 2로 45이기 때문에
    nums += [i] * i
print(sum(nums[a - 1:b]))