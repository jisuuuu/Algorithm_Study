#다면체
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    print(2 - v + e)