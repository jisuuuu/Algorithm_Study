#체스판 조각
import sys
n = int(sys.stdin.readline().rstrip())

row = n // 2 + 1
col = n - row + 2

print(row * col)