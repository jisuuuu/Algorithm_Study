#앵그리 창영
import sys
n, w, h = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    l = (w ** 2 + h ** 2) ** 0.5

    if x <= l:
        print('DA')
    else:
        print('NE')