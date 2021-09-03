#주사위 세개
import sys
arr = sorted(list(map(int, sys.stdin.readline().split())))

if len(set(arr)) == 3:
    print(arr[2] * 100)
elif len(set(arr)) == 2:
    print(1000 + (arr[1] * 100))
else:
    print(10000 + (arr[0] * 1000))