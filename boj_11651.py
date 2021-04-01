#좌표 정렬하기2
import sys

n = int(sys.stdin.readline().rstrip())
ans = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    ans.append((x, y))

ans = sorted(ans, key=lambda y: (y[1], y[0])) #다중조건


for a in ans:
    print(f'{a[0]} {a[1]}')