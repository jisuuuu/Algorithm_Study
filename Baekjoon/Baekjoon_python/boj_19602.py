#Dog Treats
import sys
s = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
l = int(sys.stdin.readline().rstrip())

if s + 2 * m + 3 * l >= 10:
    print('happy')
else:
    print('sad')