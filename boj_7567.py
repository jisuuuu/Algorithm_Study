#그릇
import sys
bowl = sys.stdin.readline().rstrip()
total = 10
before_bowl = bowl[0]

for i in range(1, len(bowl)):
    if before_bowl != bowl[i]:
        total += 10
    else:
        total += 5
    before_bowl = bowl[i]
print(total)