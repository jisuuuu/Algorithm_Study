#뒤집은 소수
import math


def reverse(x):
    num = ''

    for i in range(len(x) - 1, -1, -1):
        if i == len(x) - 1 and x[i] == '0':
            continue
        num += x[i]
    return int(num)


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/14. 뒤집은 소수/in{j}.txt', 'r')
    n = int(f.readline())
    arr = list(f.readline().split())

    result = ''
    for a in arr:
        x = reverse(a)
        if isPrime(x):
            result += str(x) + ' '
    else:
        result = result.rstrip()

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/14. 뒤집은 소수/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()