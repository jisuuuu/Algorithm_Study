#TGN
import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().rstrip().split())

    if r > e - c:
        print('do not advertise')
    elif r < e - c:
        print('advertise')
    else:
        print('does not matter')