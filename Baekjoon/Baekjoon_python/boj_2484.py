#주사위 네개
import sys
n = int(sys.stdin.readline().rstrip())
prices = []

for _ in range(n):
    nums = list(sorted(map(int, sys.stdin.readline().rstrip().split())))

    if len(set(nums)) == 1:
        price = 50000 + 5000 * nums[0]
    elif len(set(nums)) == 2:
        if nums[1] == nums[2]:
            price = 10000 + 1000 * nums[1]
        else:
            price = 2000 + (nums[1] + nums[2]) * 500
    elif len(set(nums)) == 4:
        price = max(nums) * 100
    else:
        for i in range(3):
            if nums[i] == nums[i + 1]:
                price = 1000 + nums[i] * 100
    prices.append(price)

print(max(prices))