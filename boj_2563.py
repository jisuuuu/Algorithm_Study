#색종이
import sys
n = int(sys.stdin.readline().rstrip())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

answer = 0
for p in paper:
    answer += p.count(1)
print(answer)