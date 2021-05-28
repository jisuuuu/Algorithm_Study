#배열 합치기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr_a = list(map(int, sys.stdin.readline().rstrip().split()))
arr_b = list(map(int, sys.stdin.readline().rstrip().split()))

a, b = 0, 0
res = []

while True:
    if arr_a[a] < arr_b[b]:
        res.append(arr_a[a])
        a += 1
    elif arr_a[a] > arr_b[b]:
        res.append(arr_b[b])
        b += 1
    else:
        res.append(arr_a[a])
        res.append(arr_b[b])
        a += 1
        b += 1

    if a == n or b == m:
        break
if a != n:
    for i in range(a, len(arr_a)):
        res.append(arr_a[i])
elif b != m:
    for i in range(b, len(arr_b)):
        res.append(arr_b[i])
for i in range(len(res)):
    print(res[i], end=' ')