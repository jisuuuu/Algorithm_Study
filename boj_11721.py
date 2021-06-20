#열 개씩 끊어 출력하기
import sys
string = sys.stdin.readline().rstrip()
cnt = 0

for s in string:
    if cnt < 10:
        print(s, end='')
        cnt += 1
    else:
        cnt = 1
        print()
        print(s, end='')