#Jolly Jumpers


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/24. Jolly Jumpers/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    nums = list(map(int, f.readline().rstrip().split()))
    check = [0 for _ in range(n)] # 1 - n-1 까지 있는 거니까 0은 빼고 1 - n-1
    pre = nums[0]

    result = ''

    for i in range(1, n):
        pos = abs(pre - nums[i])

        if (0 < pos < n) and check[pos] == 0:
            check[pos] = 1
        else:
            result = 'NO'
            break
        pre = nums[i]
    else:
        result = 'YES'
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/24. Jolly Jumpers/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()