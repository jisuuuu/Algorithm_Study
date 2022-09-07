#성택이의 은밀한 비밀번호
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    pw = sys.stdin.readline().rstrip()

    if 6 <= len(pw) <= 9:
        print('yes')
    else:
        print('no')