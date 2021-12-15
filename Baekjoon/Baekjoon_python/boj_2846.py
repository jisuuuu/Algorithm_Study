#오르막길
import sys
n = int(sys.stdin.readline().rstrip())
roads = list(map(int, sys.stdin.readline().rstrip().split()))
up_roads = []
total = 0

for i in range(1, n):
    if roads[i - 1] < roads[i]:
        total += (roads[i] - roads[i - 1])
    else:
        if total != 0:
            up_roads.append(total)
        total = 0
else:
    if total != 0:
        up_roads.append(total)

if up_roads:
    print(max(up_roads))
else:
    print(0)