#지영 공주님의 마법 거울
import sys
n = int(sys.stdin.readline().rstrip())
mirror = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
k = int(sys.stdin.readline().rstrip())

if k == 1:
    for i in range(n):
        for j in range(n):
            print(mirror[i][j], end='')
        print()
elif k == 2:
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(mirror[i][j], end='')
        print()
elif k == 3:
    for i in range(n - 1, -1, -1):
        for j in range(n):
            print(mirror[i][j], end='')
        print()