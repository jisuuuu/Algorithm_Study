#수빈이와 수열
import sys
n = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split(' ')))
a = [b[0]]

for i in range(1, n):
    a.append(b[i] * (i + 1) - sum(a))
print(*a)
