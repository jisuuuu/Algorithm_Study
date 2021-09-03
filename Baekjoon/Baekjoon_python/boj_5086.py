#배수와 약수
import sys

while True:
    n_1, n_2 = map(int, sys.stdin.readline().rstrip().split())
    if n_1 == 0 and n_2 == 0:
        break

    if n_1 % n_2 == 0:
        print('multiple')
    elif n_2 % n_1 == 0:
        print('factor')
    else:
        print('neither')