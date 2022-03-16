#연길이의 이상형
import sys
yg = sys.stdin.readline().rstrip()

for a in yg:
    if a == 'E':
        print('I', end='')
    elif a == 'I':
        print('E', end='')
    elif a == 'S':
        print('N', end='')
    elif a == 'N':
        print('S', end='')
    elif a == 'F':
        print('T', end='')
    elif a == 'T':
        print('F', end='')
    elif a == 'J':
        print('P', end='')
    elif a == 'P':
        print('J', end='')
print()