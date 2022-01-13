#오늘도 졌다
import sys
z = list(map(int, sys.stdin.readline().rstrip().split()))
s = list(map(int, sys.stdin.readline().rstrip().split()))
z_total = s_total = 0

for i in range(9):
    z_total += z[i]

    if z_total > s_total:
        print('Yes')
        break

    s_total += s[i]

else:
    print('No')