#정수의 개수
import sys
string = sys.stdin.readline().rstrip().split(',')
cnt = 0

for s in string:
    if s.isdigit():
        cnt += 1
print(cnt)