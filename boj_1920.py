#수 찾기
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().rstrip().split()))

for c in check:
    if c in arr:
        print(1)
    else:
        print(0)