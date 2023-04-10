#너의 평점은
import sys
grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
          }

total = 0
cnt = 0
for _ in range(20):
    scores = sys.stdin.readline().rstrip().split()

    if scores[2] != 'P':
        cnt += float(scores[1])
        total += grades[scores[2]] * float(scores[1])
print(f'{total / cnt:.6f}')