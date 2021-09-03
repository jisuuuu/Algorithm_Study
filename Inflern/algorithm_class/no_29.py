#3의 개수는(small)

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/29. 3의 개수는(small)/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    res = 1

    for i in range(n):
        res *= (i + 1)
    res = str(res)

    cnt = 0
    max_cnt = 0
    tmp = '0'
    for k in range(len(res) - 1, -1, -1):
        if tmp == '0':
            if res[k] == '0':
                cnt += 1
            else:
                cnt = 0
        tmp = res[k]

        if max_cnt < cnt:
            max_cnt = cnt
    print(max_cnt)

    f.close()

    # f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/29. 3의 개수는(small)/out{j}.txt', 'rt')
    # answer = f.read()
    # if answer == str(max_cnt):
    #     print('Ok')
    # else:
    #     print('No')
    # f.close()