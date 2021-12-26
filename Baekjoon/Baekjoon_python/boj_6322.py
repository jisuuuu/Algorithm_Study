#직각 삼각형의 두 변
import sys

idx = 1
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == b == c == 0:
        break

    check = ''

    if c == -1:
        answer = pow(a, 2) + pow(b, 2)
        check = 'c'
    elif b == -1:
        answer = pow(c, 2) - pow(a, 2)
        check = 'b'
    elif a == -1:
        answer = pow(c, 2) - pow(b, 2)
        check = 'a'

    print(f'Triangle #{idx}')
    if answer <= 0:
        print('Impossible.')
    else:
        print(f'{check} = ', end='')
        print('{:.3f}'.format(pow(answer, 0.5)))
    print()
    idx += 1