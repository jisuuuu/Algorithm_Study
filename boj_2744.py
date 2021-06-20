#대소문자바꾸기
import sys
string = sys.stdin.readline().rstrip()
for s in string:
    if 65 <= ord(s) <= 90:
        print(s.lower(), end='')
    else:
        print(s.upper(), end='')