#세수정렬
import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for a in arr:
    print(a, end=' ')