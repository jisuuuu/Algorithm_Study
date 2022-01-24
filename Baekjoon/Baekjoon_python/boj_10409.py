#서버
import sys
n, T = map(int, sys.stdin.readline().rstrip().split())
tasks = list(map(int, sys.stdin.readline().rstrip().split()))
total = 0

for i in range(n):
    if sum(tasks[:i + 1]) > T:
        print(i)
        break
else:
    print(n)