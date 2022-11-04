#행렬 덧셈
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for aa in a:
    print(*aa)