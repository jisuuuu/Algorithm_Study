#층간소음


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/18. 층간소음/in{j}.txt', 'r')
    n, m = map(int, f.readline().rstrip().split())
    arr = list(map(int, f.readline().rstrip().split()))

    cnt = 0
    res = 0
    for a in arr:
        if a > m:
            cnt += 1

            if res < cnt:
                res = cnt
            continue
        cnt = 0

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/18. 층간소음/out{j}.txt', 'rt')
    answer = f.read()
    if answer == str(res):
        print('Ok')
    else:
        print('No')
    f.close()