#화성 수학
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    arr = sys.stdin.readline().rstrip().split()
    num = float(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == '@':
            num *= 3
        elif arr[i] == '%':
            num += 5
        elif arr[i] == '#':
            num -= 7

    print('{:.2f}'.format(num))