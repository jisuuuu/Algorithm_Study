#게임을 만든 동준이
import sys
n = int(sys.stdin.readline().rstrip())
scores = []
cnt = 0

for _ in range(n):
    scores.append(int(sys.stdin.readline().rstrip()))

for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        cnt += scores[i] - scores[i + 1] + 1
        scores[i] = scores[i + 1] - 1
print(cnt)
