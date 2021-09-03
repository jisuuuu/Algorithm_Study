#나이계산


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/5. 나이계산/in{j}.txt', 'r')
    a = f.readline()
    arr = a.split('-')

    gender = ''
    year = ''
    if arr[1][0] == '1':
        gender = 'M'
        year = '19' + arr[0][0] + arr[0][1]
    elif arr[1][0] == '3':
        gender = 'M'
        year = '20' + arr[0][0] + arr[0][1]
    elif arr[1][0] == '2':
        gender = 'W'
        year = '19' + arr[0][0] + arr[0][1]
    elif arr[1][0] == '4':
        gender = 'W'
        year = '20' + arr[0][0] + arr[0][1]

    result = f'{2019 - int(year) + 1} {gender}'

    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/5. 나이계산/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()