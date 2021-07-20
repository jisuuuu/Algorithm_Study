#점수 계산
import sys
scores = [(i + 1, int(sys.stdin.readline().rstrip())) for i in range(8)]
new = sorted(scores, key=lambda x:x[1], reverse=True)
total = 0
idx = []
for i in range(5):
    total += new[i][1]
    idx.append(new[i][0])
print(total)
print(' '.join(map(str, sorted(idx))))