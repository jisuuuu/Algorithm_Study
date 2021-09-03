#평균 점수
import sys

scores = []
for _ in range(5):
    scores.append(int(sys.stdin.readline().rstrip()))

for i, s in enumerate(scores):
    if s < 40:
        scores[i] = 40

print(sum(scores) // 5)