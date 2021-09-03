#마라톤

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/26. 말아톤/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    c = list(map(int, f.readline().rstrip().split()))
    result = '1 '

    for i in range(1, n):
        cnt = 1
        for k in range(i - 1, -1, -1):
            if c[i] <= c[k]:
                cnt += 1
        result += f'{cnt} '
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/26. 말아톤/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()