#Buffoon
import sys
n = int(sys.stdin.readline().rstrip())
arr = []
max_num = 0

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    arr.append(num)

    if num > max_num:
        max_num = num

if max_num == arr[0]:
    print('S')
else:
    print('N')