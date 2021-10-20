#할로윈의 사탕
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    c, v = map(int, sys.stdin.readline().rstrip().split())
    print(f'You get {c // v} piece(s) and your dad gets {c % v} piece(s).')