#8진수, 10진수, 16진수
import sys
x = sys.stdin.readline().rstrip()

if x[0] == '0':
    if x[1] != 'x':
        print(int('0o' + x, 8))
    else:
        print(int(x, 16))
else:
    print(x)
