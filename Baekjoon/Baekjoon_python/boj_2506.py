#점수계산
import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

total = 0
score = 1
before = False

for n in nums:
    if n == 1:
        if before:
            score += 1
            total += score
        else:
            before = True
            total += score
    else:
        before = False
        score = 1
print(total)