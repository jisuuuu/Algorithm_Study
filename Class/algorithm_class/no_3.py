#진약수의 합


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/3. 진약수의 합/in{j}.txt', 'r')
    memo = f.read()

    total = 1
    result = '1'
    n = int(memo)

    for i in range(2, n):
        if n % i == 0:
            total += i
            result += f' + {i}'

    result += f' = {total}'
    print(result)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/3. 진약수의 합/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()