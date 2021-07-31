#요세푸스 문제
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(1, n + 1)]
result = []
num = k - 1

for i in range(n):
    if len(arr) <= num:
        num = num % len(arr)
    result.append(arr.pop(num))
    num += k - 1
print('<%s>' %(', '.join(list(map(str, result)))))