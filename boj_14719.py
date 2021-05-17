import sys
h, w = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

max_h = 1
max_idx = -1
for i in range(len(arr)):
    if max_h < arr[i]:
        max_h = arr[i]
        max_idx = i

result = 0
tmp = 0
for i in range(max_idx + 1):
    if arr[i] > tmp:
        tmp = arr[i]
    result += tmp

tmp = 0
for i in range(w - 1, max_idx, -1):
    if arr[i] > tmp:
        tmp = arr[i]
    result += tmp

print(result - sum(arr))