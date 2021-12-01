#스캐너
import sys
R, C, ZR, ZC = map(int, sys.stdin.readline().rstrip().split())
paper = []
scanner = []

for _ in range(R):
    paper.append(sys.stdin.readline().rstrip())

for i in range(R):
    row = []

    for j in range(C):
        row.append(paper[i][j] * ZC)

    for _ in range(ZR):
        scanner.append(row)

for s in scanner:
    print(''.join(s))