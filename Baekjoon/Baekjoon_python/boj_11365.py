#!밀비 급일
import sys
while True:
    word = sys.stdin.readline().rstrip()

    if word == 'END':
        break

    print(''.join(reversed(list(word))))