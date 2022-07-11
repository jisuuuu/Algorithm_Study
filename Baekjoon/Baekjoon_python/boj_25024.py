#시간과 날짜
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if 0 <= x <= 23 and 0 <= y <= 59:
        print('Yes ', end='')
    else:
        print('No ', end='')

    if 1 <= x <= 12:
        if x in (4, 6, 9, 11):
            if 1 <= y <= 30:
                print('Yes')
            else:
                print('No')
        elif x == 2:
            if 1 <= y <= 29:
                print('Yes')
            else:
                print('No')
        else:
            if 1 <= y <= 31:
                print('Yes')
            else:
                print('No')
    else:
        print('No')