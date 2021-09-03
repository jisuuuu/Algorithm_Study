#아나그램(구글)
from collections import Counter


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/16. 아나그램(구글)/in{j}.txt', 'r')
    str_1 = f.readline().rstrip('\n')
    str_2 = f.readline()

    counter_1 = Counter(str_1)
    counter_2 = Counter(str_2)

    result = ''
    if counter_2 == counter_1:
        result = 'YES'
    else:
        result = 'NO'

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/16. 아나그램(구글)/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()