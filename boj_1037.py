#약수
import sys
n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
print(arr[0] * arr[-1])