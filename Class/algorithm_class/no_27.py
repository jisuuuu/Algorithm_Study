#N! 표현법

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/27. N! 표현법/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    check = [0 for _ in range(n + 1)]
    #팩토리얼을 계산하고 소인수분해하는 것이 아니라 n까지 증가하며 소인수 분해한다.
    for i in range(2, n + 1):
        tmp = i
        k = 2

        while tmp != 1:
            if tmp % k == 0:
                tmp = tmp // k
                check[k] += 1
            else:
                k += 1

    result = f'{n}! = '

    for i in range(2, n + 1):
        if check[i] != 0:
            result += f'{check[i]} '

    result = result.rstrip()

    print(result)

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/27. N! 표현법/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()