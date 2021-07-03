#파티가 끝나고 난 뒤
import sys
l, p = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
real_num = l * p

for a in arr:
    print(a - real_num, end=' ')