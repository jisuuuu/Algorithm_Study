#OX퀴즈
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())

    sum = 0
    cnt = 1
    for t in temp:
        if t == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)