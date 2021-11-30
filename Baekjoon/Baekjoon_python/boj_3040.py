#백설 공주와 일곱 난쟁이
import sys
arr = []
check = [0 for _ in range(9)]
for _ in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

total = sum(arr) - 100
find = 0
for i in range(8):
    for j in range(1, 9):
        if arr[i] + arr[j] == total:
            check[i] = check[j] = 1
            find = 1

    if find:
        break

print('\n'.join([str(arr[i]) for i in range(9) if check[i] == 0]))
