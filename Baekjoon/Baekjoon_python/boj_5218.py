#알파벳 거리
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x, y = sys.stdin.readline().rstrip().split()
    print('Distances: ', end='')
    for i in range(len(x)):
        if ord(y[i]) - ord(x[i]) >= 0:
            print(ord(y[i]) - ord(x[i]), end=' ')
        else:
            print(ord(y[i]) - ord(x[i]) + 26, end=' ')
    print()