#첫 글자를 대문자로
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(word[0].upper(), end='')
    print(word[1:])