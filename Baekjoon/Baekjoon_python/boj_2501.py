#약수 구하기
import sys


n, k = map(int, sys.stdin.readline().rstrip().split())
nums = []

for i in range(1, n + 1):
    if n % i == 0:
        nums.append(i)
#효율성 생각해서 sqrt으로 동시에 넣어준 다음에 sort 했는데 sort에서 시간이 오래걸리는지 틀림
if len(nums) < k:
    print(0)
else:
    print(nums[k - 1])