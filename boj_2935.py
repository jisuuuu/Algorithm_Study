import sys

a = int(sys.stdin.readline().rstrip())
c = sys.stdin.readline().rstrip()
b = int(sys.stdin.readline().rstrip())

if c == '*':
    print(f'{a * b}')
else:
    print(f'{a + b}')