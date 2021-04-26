#영어단어 복구
import math


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/7. 영어단어 복구/in{j}.txt', 'r')
    word = f.read()
    word = word.replace(' ', '')
    result = f'{word.lower()}'

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/7. 영어단어 복구/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()