#평균
import sys
n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))

m = max(num)
for i in range(n):
    num[i] = num[i] / m * 100

print(sum(num) / n)