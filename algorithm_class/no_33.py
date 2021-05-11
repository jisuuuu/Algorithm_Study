#3등의 성적은
from collections import deque


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/33. 3등의 성적은/in{j}.txt', 'r')
    n = int(f.readline().rstrip())
    arr = list(map(int, f.readline().rstrip().split()))

    for i in range(0, n - 1):
        idx = i

        for k in range(i + 1, n):
            if arr[k] > arr[idx]:
                idx = k
        arr[i], arr[idx] = arr[idx], arr[i]

    cnt = 1
    tmp = arr[0]
    result = ''
    for i in range(1, n):
        if arr[i] != tmp:
            cnt += 1
            if cnt == 3:
                result = str(arr[i])
                break
        tmp = arr[i]

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/33. 3등의 성적은/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()