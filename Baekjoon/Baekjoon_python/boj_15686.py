#치킨 배달
import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().rstrip().split())
map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
house, chicken = [], []
result = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 2:
            chicken.append((i, j))
        elif map[i][j] == 1:
            house.append((i, j))

for pick_chicken in combinations(chicken, m):
    total = 0
    for hx, hy in house:
        temp = sys.maxsize
        for cx, cy in pick_chicken:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        total += temp
    result.append(total)
print(min(result))