#Divvying Up
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

if sum(arr) % 3 != 0:
    print('no')
else:
    print('yes')