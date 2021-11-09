#홀수일까 짝수일까
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    k = int(sys.stdin.readline().rstrip())

    if k % 2 == 0:
        print('even')
    else:
        print('odd')