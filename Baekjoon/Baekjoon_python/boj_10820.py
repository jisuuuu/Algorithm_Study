#문자열 분석
import sys
while True:
    strings = sys.stdin.readline().rstrip('\n')
    lower, upper, number, null = 0, 0, 0, 0

    if not strings:
        break

    for s in strings:
        if s.isupper():
            upper += 1
        elif s.islower():
            lower += 1
        elif s.isdigit():
            number += 1
        elif s.isspace():
            null += 1

    print(f'{lower} {upper} {number} {null}')