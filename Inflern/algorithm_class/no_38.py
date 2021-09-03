#inversion sequence

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/38. inversion sequence/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    arr = list(map(int, f.readline().rstrip().split()))
    tmp = [0 for _ in range(n)]

    cnt = n

    for i in range(n - 1, -1, -1):
        tmp[i] = cnt

        for k in range(i, i + arr[i]):
            tmp[k], tmp[k + 1] = tmp[k + 1], tmp[k]

        cnt -= 1

    print(tmp)
    tmp = list(map(str, tmp))
    result = ' '.join(tmp)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/38. inversion sequence/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()