#별찍기
import sys
n = int(sys.stdin.readline().rstrip())
matrix = [[' ' for _ in range(n)] for _ in range(n)]


def makeStar(x, y, num):
    if num == 1:
        matrix[x][y] = '*'
        return
    value = int(num / 3)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                makeStar(x + (value * i), y + (value * j), value)
                # (0, 0) (3, 0) (6, 0) 이 같음
                # (0, 0) (0, 3) (0, 6) 이 같음


makeStar(0, 0, n)

for i in range(n):
    s = ''
    for j in range(n):
        s += matrix[i][j]
    print(s)