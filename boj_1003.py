#피보나치 함수
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x = int(sys.stdin.readline().rstrip())
    zero_cnt = 1
    one_cnt = 0
    tmp = 0
    for _ in range(x):
        tmp = one_cnt
        one_cnt += zero_cnt
        zero_cnt = tmp

    print(zero_cnt, one_cnt)