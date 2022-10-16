#진법 변환
import sys
n, b = sys.stdin.readline().rstrip().split()
n = ''.join(reversed(n))
b = int(b)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0

for i in range(len(n) - 1, -1, -1):
    result += number.index(n[i]) * (b ** i)
print(result)