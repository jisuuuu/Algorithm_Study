#모두의 약수

import math

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/9. 모두의 약수/in{j}.txt', 'r')
    n = int(f.read())
    result = ''

    for i in range(1, n + 1):
        cnt = 0

        for k in range(1, int(math.sqrt(i)) + 1):
            if i % k == 0:
                cnt += 1
                if k != (i // k):
                    cnt += 1

        result += f'{cnt} '
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/9. 모두의 약수/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()