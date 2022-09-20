#공약수
import sys
n = int(sys.stdin.readline().rstrip())

if n == 2:
    a, b = map(int, sys.stdin.readline().rstrip().split())

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            print(i)
elif n == 3:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            print(i)