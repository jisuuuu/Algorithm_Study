#새
import sys
n = int(sys.stdin.readline().rstrip())
result = 0
k = 1

while n > 0:
    if n < k:
        k = 1
    n -= k
    k += 1
    result += 1

print(result)