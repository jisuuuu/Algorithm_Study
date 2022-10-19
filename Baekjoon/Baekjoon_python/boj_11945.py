#뜨거운 붕어빵
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    bread = sys.stdin.readline().rstrip()
    print(bread[::-1])