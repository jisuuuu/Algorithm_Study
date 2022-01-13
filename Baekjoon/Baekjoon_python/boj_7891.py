#Can you add this?
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(x + y)