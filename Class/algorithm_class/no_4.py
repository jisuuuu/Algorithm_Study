#나이 차이


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/4. 나이차이/in{j}.txt', 'r')
    n = f.readline()
    arr = list(map(int, f.readline().split()))

    result = max(arr) - min(arr)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/4. 나이차이/out{j}.txt', 'r')
    answer = int(f.read())

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()