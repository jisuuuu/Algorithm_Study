#보물
import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
b.sort(reverse=True)

total = 0
for i in range(n):
    total += (a[i] * b[i])
print(total)