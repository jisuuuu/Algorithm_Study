#단어 퍼즐
import sys
i = 1
while True:
    a = list(sys.stdin.readline().rstrip())
    b = list(sys.stdin.readline().rstrip())

    if ''.join(b) == 'END' and ''.join(a) == 'END':
        break

    print(f'Case {i}: ', end='')
    if sorted(a) == sorted(b):
        print('same')
    else:
        print('different')
    i += 1