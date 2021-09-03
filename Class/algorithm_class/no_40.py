#교집합
for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/40. 교집합/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    n_arr = list(map(int, f.readline().rstrip().split()))
    m = int(f.readline().rstrip())
    m_arr = list(map(int, f.readline().rstrip().split()))

    n_arr.sort()
    m_arr.sort()

    i, k = 0, 0
    new = []
    while i < n and k < m:
        if n_arr[i] == m_arr[k]:
            new.append(n_arr[i])
            i += 1
            k += 1
        elif n_arr[i] < m_arr[k]:
            i += 1
        else:
            k += 1
    new = list(map(str, new))

    result = ' '.join(new)

    print(result)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/40. 교집합/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()