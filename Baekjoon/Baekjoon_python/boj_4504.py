#배수 찾기
import sys
n = int(sys.stdin.readline().rstrip())
tmp = int(sys.stdin.readline().rstrip())

while tmp:
    if tmp % n == 0:
        print(f'{tmp} is a multiple of {n}.')
    else:
        print(f'{tmp} is NOT a multiple of {n}.')

    tmp = int(sys.stdin.readline().rstrip())