#Identifying tea
import sys
t = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(arr.count(t))