#수열의 변화
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
a_nums = list(map(int, sys.stdin.readline().rstrip().split(',')))

for _ in range(k):
    b_nums = [a_nums[i + 1] - a_nums[i] for i in range(len(a_nums) - 1)]
    a_nums = b_nums
print(*a_nums, sep=',')