#비교 연산자
import sys
i = 0
while True:
    i += 1
    a, x, b = sys.stdin.readline().rstrip().split()
    if 'E' in x:
        break
    print(f'Case {i}: ', end='')
    if x == '>':
        result = int(a) > int(b)
    elif x == '<':
        result = int(a) < int(b)
    elif x == '>=':
        result = int(a) >= int(b)
    elif x == '<=':
        result = int(a) <= int(b)
    elif x == '==':
        result = int(a) == int(b)
    elif x == '!=':
        result = int(a) != int(b)

    if result:
        print('true')
    else:
        print('false')