#가장 많이 사용된 자릿수
from collections import Counter


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/13. 가장 많이 사용된 자릿수/in{j}.txt', 'r')
    n = list(f.read())
    ans = ''

    result = Counter(n)
    new = list(result.values())
    if new.count(max(new)) == 1:
        ans = result.most_common(n=1)[0][0]
    else:
        max_num = max(new)
        tmp = -1
        for k, v in result.items():
            if v == max_num and tmp < int(k):
                tmp = int(k)

        ans = str(tmp)
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/13. 가장 많이 사용된 자릿수/out{j}.txt', 'r')
    answer = f.read()

    if answer == ans:
        print('Ok')
    else:
        print('No')
    f.close()