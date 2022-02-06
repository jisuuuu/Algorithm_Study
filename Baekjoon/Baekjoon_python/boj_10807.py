#개수 세기
import sys
n = int(sys.stdin.readline().rstrip())
nums = map(int, sys.stdin.readline().rstrip().split())
v = int(sys.stdin.readline().rstrip())
cnt = 0

for nm in nums:
    if nm == v:
        cnt += 1
print(cnt)