#직각삼각형
import sys
while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    if sum(arr) == 0:
        break

    max_num = max(arr)
    arr.remove(max_num)

    if arr[0] ** 2 + arr[1] ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')