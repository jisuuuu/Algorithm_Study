#올바른 괄호


for j in range(1, 6):
    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/8. 올바른 괄호/in{j}.txt', 'r')
    arr = list(f.read())
    stack = []
    result = ''

    for a in arr:
        if a == ')':
            if stack and stack.pop() == '(':
                continue
            else:
                result = 'NO'
                break
        else:
            stack.append(a)
    else:
        if len(stack) == 0:
            result = 'YES'
        else:
            result = 'NO'
    f.close()

    f = open(f'D:/알고리즘 강의자료/CPS(채점폴더)/8. 올바른 괄호/out{j}.txt', 'r')
    answer = f.read()

    if answer == result:
        print('Ok')
    else:
        print('No')
    f.close()