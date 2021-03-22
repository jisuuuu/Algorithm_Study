#한수
import sys

n = int(sys.stdin.readline().rstrip())
check = 0

for i in range(1, n + 1):
    if i < 100: #1, 2 자리수는 등차수열을 비교할 수 없으므로 모두 한수
        check += 1
    else:
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            check += 1

print(check)