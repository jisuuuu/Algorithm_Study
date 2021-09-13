# 럭키 스트레이트
import sys
n = sys.stdin.readline().rstrip()
left_total, right_total = 0, 0

for i in range(len(n) // 2):
    left_total += int(n[i])
    right_total += int(n[len(n) - i - 1])

if left_total == right_total:
    print('LUCKY')
else:
    print('READY')