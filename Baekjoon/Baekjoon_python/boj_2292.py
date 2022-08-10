#벌집
import sys
n = int(sys.stdin.readline().rstrip())
bee_house = 1
cnt = 1

while n > bee_house:
    bee_house += 6 * cnt
    cnt += 1
print(cnt)