# 덩치
import sys
n = int(sys.stdin.readline().rstrip())
people = []

for _ in range(n):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    people.append((w, h))

for p1 in people:
    rank = 1

    for p2 in people:
        if (p1[0] < p2[0]) and (p1[1] < p2[1]):
            rank += 1
    print(rank, end=' ')