#숫자의 총 개수(small)


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/11. 숫자의 총 개수(small)/in{j}.txt', 'r')
    n = int(f.read())
    cnt = 0
    check = 9
    digit = 1

    while n > check:
        cnt += check * digit
        n = n - check
        check = check * 10
        digit += 1

    cnt += n * digit

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/11. 숫자의 총 개수(small)/out{j}.txt', 'r')
    answer = f.read()

    if answer == str(cnt):
        print('Ok')
    else:
        print('No')
    f.close()