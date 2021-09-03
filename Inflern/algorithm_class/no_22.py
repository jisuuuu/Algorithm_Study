#온도의 최대값


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/22. 온도의 최대값/in{j}.txt', 'r')
    n, k = map(int, f.readline().rstrip().split())
    nums = list(map(int, f.readline().rstrip().split()))
    total = 0

    for i in range(k):#이중 for문을 사용하지 않고 O(n)으로 푸는 방법
        total += nums[i]

    result = -99999 #모든 값이 -일 수 있으므로 초기값 -99999로 하지 않고 0으로 초기화하면 0이 출력
    for r in range(k, n):
        total += (nums[r] - nums[r - k])
        if result < total:
            result = total

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/22. 온도의 최대값/out{j}.txt', 'rt')
    answer = f.read()
    if answer == str(result):
        print('Ok')
    else:
        print('No')
    f.close()