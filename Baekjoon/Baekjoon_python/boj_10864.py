#친구
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
students = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    students[a - 1] += 1
    students[b - 1] += 1

for s in students:
    print(s)