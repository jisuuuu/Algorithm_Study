#감소하는 수
import sys

n = int(sys.stdin.readline().rstrip())

if n >= 1023: # 가장 큰 감소하는 수 : 9876543210
    print(-1) # idx : 1022
elif n == 0:
    print(0)
else:
    cnt = 0
    num = 1

    while True:
        str_num = str(num)
        flag = True

        if len(str_num) == 1: #길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue
                else:
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i  + 1:]

                    num = int(start + mid + end)
                    print(f'{start} + {mid} + {end}')
                    flag = False
                    break

        if flag:
            cnt += 1
            if cnt == n:
                break
            num += 1

    print(num)