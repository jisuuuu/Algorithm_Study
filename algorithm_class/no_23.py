#연속 부분 증가수열


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/23. 연속 부분 증가수열/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    nums = list(map(int, f.readline().rstrip().split()))
    cnt = 1
    tmp = nums[0]
    result = -1
    for i in range(1, n):
        if tmp <= nums[i]:
            cnt += 1
            if result < cnt:
                result = cnt
        else:
            cnt = 1
        tmp = nums[i]
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/23. 연속 부분 증가수열/out{j}.txt', 'rt')
    answer = f.read()
    if answer == str(result):
        print('Ok')
    else:
        print('No')
    f.close()