#수열의 변화
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
a_nums = list(map(int, sys.stdin.readline().rstrip().split(',')))

for _ in range(k):
    b_nums = [a_nums[i] - a_nums[i - 1] for i in range(1, len(a_nums))]
    a_nums = b_nums
print(*b_nums, sep=',')