#ATM
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

total = 0
for i in range(len(arr) + 1):
    for j in range(i):
        total += arr[j]
print(total)