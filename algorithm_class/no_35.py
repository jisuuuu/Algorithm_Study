#Special Sort


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/35. Special Sort/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    arr = list(map(int, f.readline().rstrip().split()))

    for i in range(len(arr) - 1):
        for k in range(len(arr) - 1 - i):
            if arr[k] > 0 and arr[k + 1] < 0:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    arr = list(map(str, arr))
    result = ' '.join(arr)

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/35. Special Sort/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()