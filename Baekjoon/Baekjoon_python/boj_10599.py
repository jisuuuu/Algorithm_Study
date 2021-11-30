#페르시아의 왕들
import sys

while True:
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    print(f'{c - b} {d - a}')