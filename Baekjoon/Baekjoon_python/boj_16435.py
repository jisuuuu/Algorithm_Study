#스네이크버드
import sys
n, l = map(int, sys.stdin.readline().rstrip().split())
fruits = list(map(int, sys.stdin.readline().rstrip().split()))

fruits.sort()

for f in fruits:
    if f <= l:
        l += 1
print(l)