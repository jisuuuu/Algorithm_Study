#ROT13
import sys
S = sys.stdin.readline().rstrip()

for s in S:
    if s.isupper():
        if ord(s) + 13 > 90:
            print(chr(ord(s) - 13), end='')
        else:
            print(chr(ord(s) + 13), end='')

    elif s.islower():
        if ord(s) + 13 > 122:
            print(chr(ord(s) - 13), end='')
        else:
            print(chr(ord(s) + 13), end='')

    else:
        print(s, end='')