#단어순서 뒤집기
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []
    print(f'Case #{i + 1}: ', end='')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            print(''.join(reversed(stack)), end=' ')
            stack = []
        else:
            stack.append(s[i])
    else:
        if stack:
            print(''.join(reversed(stack)), end=' ')
    print()