#자릿수의 합


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/10. 자릿수의 합/in{j}.txt', 'r')
    n = int(f.readline())
    arr = f.readline().rstrip().split()
    res = 0
    result = ''

    for a in arr:
        new = list(map(int, a))

        if sum(new) > res:
            res = sum(new)
            result = a
        elif sum(new) == res:
            if int(result) < int(a):
                result = a

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/10. 자릿수의 합/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()