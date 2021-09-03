#숫자만 추출
import math


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/6. 숫자만 추출/in{j}.txt', 'r')
    words = f.readline()

    arr = []
    for w in words:
        if 48 <= ord(w) <= 57:
            if ord(w) == 48:
                if len(arr) > 0:
                    arr.append(w)
            else:
                arr.append(w)

    num = int(''.join(arr))
    num_n = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            num_n.append(i)
            if i != num // i:
                num_n.append(num // i)

    result = f'{num}\n{len(num_n)}'
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/6. 숫자만 추출/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()