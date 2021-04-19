#1부터 N까지의 M의 배수합
import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
for j in range(1, 6):
    total = 0

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/1. 1부터 N까지의 M의 배수합/in{j}.txt', 'r')
    memo = f.read()
    n, m = map(int, memo.split())
    for i in range(1, n + 1):
        if i % m == 0:
            total += i

    print(total)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/1. 1부터 N까지의 M의 배수합/out{j}.txt', 'r')
    num = f.read()
    num = int(num)
    print(num)

    if num == total:
        print('Ok')
    else:
        print('No')
    f.close()