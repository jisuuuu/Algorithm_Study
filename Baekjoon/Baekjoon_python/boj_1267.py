#핸드폰 요금
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

m, y = 0, 0

for a in arr:
    y += (a // 30 + 1) * 10
    m += (a // 60 + 1) * 15

if m < y:
    print(f'M {m}')
elif m > y:
    print(f'Y {y}')
else:
    print(f'Y M {y}')