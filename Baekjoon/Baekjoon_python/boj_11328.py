#Strfry
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    a = list(a)
    b = list(b)

    a.sort()
    b.sort()

    if a == b:
        print('Possible')
    else:
        print('Impossible')