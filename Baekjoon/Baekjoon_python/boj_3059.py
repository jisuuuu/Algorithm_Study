#등장하지 않는 문자의 합
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    s_list = set(sys.stdin.readline().rstrip())
    total = 2015
    for s in s_list:
        total -= ord(s)
    print(total)