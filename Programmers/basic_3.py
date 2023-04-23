# 대소문자 바꿔서 출력하기
import sys
word = sys.stdin.readline().rstrip()

for w in word:
    if w.isupper():
        print(w.lower(), end='')
    else:
        print(w.upper(), end='')