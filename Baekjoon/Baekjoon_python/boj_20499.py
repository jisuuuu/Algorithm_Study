#Darius님 한타 안 함?
import sys
k, d, a = map(int, sys.stdin.readline().rstrip().split('/'))

if d == 0 or k + a < d:
    print('hasu')
else:
    print('gosu')