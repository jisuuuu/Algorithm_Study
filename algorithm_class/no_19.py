#분노 유발자
#뒤가 기준이므로 뒤에서 부터 확인한다
#앞에서 확인하면 더 복잡하기 때문에
#자기 앞에 있는 사람이 나보다 크면 cnt++
#뒤에서 시작하기 때문에 앞사람만 체크하면 된다

for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/19. 분노 유발자/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    arr = list(map(int, f.readline().rstrip().split()))

    cnt = 0
    max_num = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if max_num < arr[i]:
            max_num = arr[i]
            cnt += 1

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/19. 분노 유발자/out{j}.txt', 'rt')
    answer = f.read()
    if answer == str(cnt):
        print('Ok')
    else:
        print('No')
    f.close()