#카드게임
def result(aa, bb):
    a = 0
    b = 0
    tmp = -1

    for i in range(len(aa)):
        if aa[i] > bb[i]:
            a += 3
            tmp = i
        elif aa[i] < bb[i]:
            b += 3
            tmp = i
        else:
            a += 1
            b += 1

    return a, b, tmp


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/21. 카드게임/in{j}.txt', 'r')
    a_arr = list(map(int, f.readline().rstrip().split()))
    b_arr = list(map(int, f.readline().rstrip().split()))

    a, b, tmp = result(a_arr, b_arr)

    res = f'{a} {b}\n'

    if a > b:
        res += 'A'
    elif a < b:
        res += 'B'
    else:
        if a_arr[len(a_arr) - 1] > b_arr[len(b_arr) - 1]:
            res += 'A'
        elif a_arr[len(a_arr) - 1] < b_arr[len(b_arr) - 1]:
            res += 'B'
        else:
            if tmp == -1:
                res += 'D'
            else:
                if a_arr[tmp] > b_arr[tmp]:
                    res += 'A'
                else:
                    res += 'B'

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/21. 카드게임/out{j}.txt', 'rt')
    answer = f.read()
    if answer == res:
        print('Ok')
    else:
        print('No')
    f.close()