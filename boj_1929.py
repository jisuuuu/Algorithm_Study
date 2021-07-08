#소수 구하기
import sys
m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [True for _ in range(n + 1)]

for i in range(2, int((n + 1) ** 0.5) + 1):
    if arr[i]:
        for j in range(2 * i, n + 1, i):
            arr[j] = False

for i in range(m, n + 1):
    if i > 1:
        if arr[i]:
            print(i)