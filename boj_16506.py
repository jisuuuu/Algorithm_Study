# CPU
# 시뮬레이션 브루트토스
import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]
answer = []

for a in arr:
    res = ['0' for _ in range(16)]
    # 4, 12 ~ 15
    if a[0][-1] == 'C':
        res[4] = '1'
        num = bin(int(a[3]))
        num_arr = list(num)
        cnt = 15
        for i in range(len(num_arr) - 1, 1, -1):
            res[cnt] = num_arr[i]
            cnt -= 1

    else:
        res[4] = '0'

        num = bin(int(a[3]))
        num_arr = list(num)
        cnt = 14
        for i in range(len(num_arr) - 1, 1, -1):
            res[cnt] = num_arr[i]
            cnt -= 1

    # 5
    res[5] = '0'

    # 9 ~ 11
    if a[0] not in ('MOV', 'MOVC', 'NOT'):
        num = bin(int(a[2]))
        num_arr = list(num)

        cnt = 11
        for i in range(len(num_arr) - 1, 1, -1):
            res[cnt] = num_arr[i]
            cnt -= 1

    # 6 ~ 8
    num = bin(int(a[1]))
    num_arr = list(num)

    cnt = 8
    for i in range(len(num_arr) - 1, 1, -1):
        res[cnt] = num_arr[i]
        cnt -= 1

    # 0 ~ 3
    if a[0] in ('ADD', 'ADDC'):
        pass
    elif a[0] in ('SUB', 'SUBC'):
        res[3] = '1'
    elif a[0] in ('MOV', 'MOVC'):
        res[2] = '1'
    elif a[0] in ('AND', 'ANDC'):
        res[3] = '1'
        res[2] = '1'
    elif a[0] in ('OR', 'ORC'):
        res[1] = '1'
    elif a[0] in ('NOT'):
        res[1] = '1'
        res[3] = '1'
    elif a[0] in ('MULT', 'MULTC'):
        res[1] = '1'
        res[2] = '1'
    elif a[0] in ('LSFTL', 'LSFTLC'):
        res[1] = '1'
        res[2] = '1'
        res[3] = '1'
    elif a[0] in ('LSFTR', 'LSFTRC'):
        res[0] = '1'
    elif a[0] in ('ASFTR', 'ASFTRC'):
        res[0] = '1'
        res[3] = '1'
    elif a[0] in ('RL', 'RLC'):
        res[0] = '1'
        res[2] = '1'
    elif a[0] in ('RR', 'RRC'):
        res[0] = '1'
        res[2] = '1'
        res[3] = '1'

    print(''.join(res))