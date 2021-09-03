#31. 탄화수소 질량
from collections import deque


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/31. 탄화수소 질량/in{j}.txt', 'r')
    n = f.read()
    q = deque(list(n))

    q.popleft()

    c_n, h_n = 0, 0

    tmp = ''
    while q[0] != 'H':
        tmp += q.popleft()

    if tmp == '':
        c_n = 1
    else:
        c_n = int(tmp)

    tmp = ''
    q.popleft()
    while q:
        tmp += q.popleft()

    if tmp == '':
        h_n = 1
    else:
        h_n = int(tmp)

    result = c_n * 12 + h_n * 1
    print(result)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/31. 탄화수소 질량/out{j}.txt', 'r')
    answer = f.read()

    if answer == str(result):
        print('Ok')
    else:
        print('No')
    f.close()