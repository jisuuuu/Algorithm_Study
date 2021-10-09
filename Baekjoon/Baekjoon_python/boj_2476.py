#주사위 게임
import sys
n = int(sys.stdin.readline().rstrip())

max_money = 0
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == b == c:
        max_money = max(max_money, 10000 + a * 1000)
    elif a == b:
        max_money = max(max_money, 1000 + a * 100)
    elif b == c:
        max_money = max(max_money, 1000 + b * 100)
    elif c == a:
        max_money = max(max_money, 1000 + c * 100)
    else:
        max_money = max(max_money, max(a, b, c) * 100)
print(max_money)