#부호
import sys
for _ in range(3):
    n = int(sys.stdin.readline().rstrip())
    total = 0

    for _ in range(n):
        total += int(sys.stdin.readline().rstrip())

    if total > 0:
        print('+')
    elif total < 0:
        print('-')
    else:
        print(0)