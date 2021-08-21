#행렬 곱셈
import sys
n, m = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
b = []
for _ in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(a)):
    temp = []
    for j in range(len(b[0])):
        t = 0
        for k in range(len(b)):
            t += a[i][k] * b[k][j]
        temp.append(t)
    print(' '.join(list(map(str, temp))))