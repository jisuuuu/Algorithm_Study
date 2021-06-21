#중복빼고 정렬하기
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(set(map(int, sys.stdin.readline().rstrip().split())))
arr.sort()
arr = list(map(str, arr))
print(' '.join(arr))