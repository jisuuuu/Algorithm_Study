#분수 좋아해?
import sys
while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0:
        break
    print(f'{a // b} {a % b} / {b}')