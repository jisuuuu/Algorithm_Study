#카드 놀이
import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a_cnt, b_cnt, last_who = 0, 0, 'D'

for i in range(10):
    if a[i] > b[i]:
        a_cnt += 3
        last_who = 'A'
    elif a[i] < b[i]:
        b_cnt += 3
        last_who = 'B'
    else:
        a_cnt += 1
        b_cnt += 1
print(a_cnt, b_cnt)

if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
else:
    print(last_who)