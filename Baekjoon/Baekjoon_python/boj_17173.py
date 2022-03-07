#배수들의 합
import sys, math
n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

for i in range(1, n + 1):
    for n in numbers:
        if i % n == 0:
            result += i
            break
print(result)