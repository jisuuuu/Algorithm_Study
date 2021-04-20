#자연수의 합
#import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/2. 자연수의 합/in{j}.txt', 'r')
    memo = f.read()

    total = 0
    result = ''
    n, m = map(int, memo.split())

    for i in range(n, m + 1):
        if i != m:
            total += i
            result += f'{i} + '
        else:
            total += i
            result += f'{i} '

    result += f'= {total}'
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/2. 자연수의 합/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()