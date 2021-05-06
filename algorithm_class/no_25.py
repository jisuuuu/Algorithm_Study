#석차 구하기

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/25. 석차 구하기/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    nums = list(map(int, f.readline().rstrip().split()))
    check = [1 for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if nums[k] > nums[i]:
                check[i] += 1

    result = ' '.join(map(str, check))
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/25. 석차 구하기/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()