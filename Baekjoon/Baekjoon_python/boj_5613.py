#계산기 프로그램
import sys
result = int(sys.stdin.readline().rstrip())
s = ''
while True:
    op = sys.stdin.readline().rstrip()
    if op == '=':
        break

    n = int(sys.stdin.readline().rstrip())

    if op == '+':
        result += n
    elif op == '-':
        result -= n
    elif op == '*':
        result *= n
    elif op == '/':
        result //= n

print(result)