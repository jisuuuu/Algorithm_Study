#Tournament Selection
import sys
cnt = 0

for _ in range(6):
    score = sys.stdin.readline().rstrip()
    if score == 'W':
        cnt += 1
if cnt >= 5:
    print(1)
elif 5 > cnt >= 3:
    print(2)
elif 3 > cnt >= 1:
    print(3)
else:
    print(-1)