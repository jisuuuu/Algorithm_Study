#선생님 퀴즈
from collections import Counter


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/17. 선생님 퀴즈/in{j}.txt', 'r')
    n = int(f.readline().rstrip())

    result = ''
    for _ in range(n):
        s, res = map(int, f.readline().rstrip().split())

        ans = s * (s + 1) // 2

        if res == ans:
            result += 'YES\n'
        else:
            result += 'NO\n'
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/17. 선생님 퀴즈/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()