
# 점수 계산
import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
scores = list(map(int, input().split()))
total = 0
cnt = 0

for s in scores:
    if s == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0

print(total)