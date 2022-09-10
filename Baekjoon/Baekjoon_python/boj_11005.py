#진법 변환2
import sys
n, b = map(int, sys.stdin.readline().rstrip().split())
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = str()

while n != 0:
    answer += system[n % b]
    n //= b
print(answer[::-1])