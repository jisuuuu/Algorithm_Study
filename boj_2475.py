# 검증수
import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0

for a in arr:
    answer += a * a
print(answer % 10)