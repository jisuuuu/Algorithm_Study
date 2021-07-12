#거꾸로 구구단
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
max_num = -1
for i in range(1, k + 1):
    num = n * i
    if max_num < int(str(num)[::-1]):
        max_num = int(str(num)[::-1])
print(max_num)