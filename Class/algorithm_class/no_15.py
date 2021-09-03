#소수의 개수
import math


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/15. 소수의 개수/in{j}.txt', 'r')
    n = int(f.read())
    prime = [True for _ in range(n + 1)]
    prime[0] = False
    prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:
            k = 2

            while i * k <= n:
                prime[i * k] = False
                k += 1

    result = str(prime.count(True))
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/15. 소수의 개수/out{j}.txt', 'rt')
    answer = f.read()
    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()