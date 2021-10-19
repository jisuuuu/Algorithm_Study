#10부제
import sys
check = sys.stdin.readline().rstrip()
arr = sys.stdin.readline().rstrip().split()

cnt = 0
for a in arr:
    if check in a:
        cnt += 1
print(cnt)