#고급 수학
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

    if nums[2] ** 2 == nums[1] ** 2 + nums[0] ** 2:
        print(f'Scenario #{i + 1}:')
        print('yes\n')
    else:
        print(f'Scenario #{i + 1}:')
        print('no\n')