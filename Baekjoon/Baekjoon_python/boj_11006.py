#남욱이의 닭장
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    u = m * 2 - n
    t = m - u
    print(u, t)