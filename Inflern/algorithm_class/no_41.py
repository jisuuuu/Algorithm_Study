#연속된 자연수의 합

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/41. 연속된 자연수의 합/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    tmp = n
    cnt, b = 0, 1
    n -= 1 #이미 1 뺀 것
    result = ''

    while n > 0:
        b += 1
        n = n - b #연속된 갯수 1, 2, 3, 4, ... ex) 15 - (1 + 2)

        if n % b == 0: # 12 % 2(연속된 갯수) == 0
            for i in range(1, b):
                result += f'{int((n / b) + i)} + ' # (6 + 1) + (6 + 2) = 7 + 8 = 15
            result += f'{int((n / b) + i + 1)} = {tmp}\n'
            cnt += 1
    result += f'{cnt}'

    print(result)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/41. 연속된 자연수의 합/out{j}.txt', 'r')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()