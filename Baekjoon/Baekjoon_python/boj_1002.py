#터렛
import sys
import math
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) **2)

    if distance == 0: # 두 원의 중심이 같은 겨우
        if r1 == r2: # 두원의 크기가 아예 같아지는 경우
            print(-1)
        else: # 한 원이 다른 원에 들어가있는 경우
            print(0)
    else: # 두원의 중심이 다른 경우
        if r1 + r2 == distance or abs(r2 - r1) == distance: # 한 점에서 겹치는 경우
            print(1)
        elif abs(r1 - r2) < distance < r1 + r2:
            print(2)
        else:
            print(0)