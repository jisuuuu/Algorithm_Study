#얼마?
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    s = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        q, p = map(int, sys.stdin.readline().rstrip().split())

        s += q * p
    print(s)