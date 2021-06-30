#나는 요리사다
import sys
idx = -1
score = -sys.maxsize

for i in range(5):
    num = sum(list(map(int, sys.stdin.readline().rstrip().split())))

    if num > score:
        idx = i + 1
        score = num
print(idx, score)