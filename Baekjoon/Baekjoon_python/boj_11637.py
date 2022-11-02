#인기 투표
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    max_cnt = arr.count(max(arr))
    max_num = max(arr)

    if max_cnt != 1:
        print('no winner')
    else:
        if max(arr) > sum(arr) // 2:
            print(f'majority winner {arr.index(max_num) + 1}')
        else:
            print(f'minority winner {arr.index(max_num) + 1}')