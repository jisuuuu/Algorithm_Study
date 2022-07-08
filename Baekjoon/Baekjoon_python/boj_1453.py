# 피시방 알바
import sys
n = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().rstrip().split()))
checked = [0 for _ in range(101)]
cnt = 0

for p in people:
    if checked[p] != 0:
        cnt += 1
    else:
        checked[p] += 1
print(cnt)