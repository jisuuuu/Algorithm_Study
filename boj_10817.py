#세수
import sys

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = sorted(arr)
print(arr[1])