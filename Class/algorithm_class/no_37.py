#LRU + insertionSort
from collections import deque


def insertionSort(temp):
    for i in range(1, len(temp)):
        for j in range(i, 0, -1):
            if temp[j - 1] > temp[j]:
                temp[j - 1], temp[j] = temp[j], temp[j - 1]

    return temp


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/37. LRU/in{j}.txt', 'r')
    s, n = map(int, f.readline().rstrip().split())
    arr = list(map(int, f.readline().rstrip().split()))

    q = deque(maxlen=s)

    for a in arr:
        if a not in q:
            q.appendleft(a)
        else:
            q.remove(a)
            q.appendleft(a)
    res = list(map(str, q))
    result = ' '.join(res)
    print(result)

    new = insertionSort(arr)
    print(new)

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/37. LRU/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()