#지각
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    d = int(sys.stdin.readline().rstrip())
    n = 0

    while n + n * n <= d:
        n += 1
    print(n - 1)