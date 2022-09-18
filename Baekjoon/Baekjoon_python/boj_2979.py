#트럭 주차
import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
time = [0] * 101

for i in range(3):
    start, end = map(int, sys.stdin.readline().rstrip().split())

    for j in range(start - 1, end - 1):
        time[j] += 1

answer = 0

for t in time:
    if t == 1:
        answer += a * t
    elif t == 2:
        answer += b * t
    elif t == 3:
        answer += c * t
print(answer)