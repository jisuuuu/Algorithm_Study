#가위 바위 보

def result(a, b):
    if a == 1:
        if b == 1:
            return 'D'
        elif b == 2:
            return 'B'
        else:
            return 'A'
    elif a == 2:
        if b == 1:
            return 'A'
        elif b == 2:
            return 'D'
        else:
            return 'B'
    elif a == 3:
        if b == 1:
            return 'B'
        elif b == 2:
            return 'A'
        else:
            return 'D'


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/20. 가위바위보/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    a_arr = list(map(int, f.readline().rstrip().split()))
    b_arr = list(map(int, f.readline().rstrip().split()))
    res = ''

    for i in range(n):
        res += result(a_arr[i], b_arr[i])
        res += '\n'
    res = res.rstrip()

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/20. 가위바위보/out{j}.txt', 'rt')
    answer = f.read()
    if answer == res:
        print('Ok')
    else:
        print('No')
    f.close()