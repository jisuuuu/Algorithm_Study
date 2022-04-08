#5의 수난
import sys
nums = list(map(int, list(sys.stdin.readline().rstrip())))
total = 0

for n in nums:
    total += n ** 5
print(total)