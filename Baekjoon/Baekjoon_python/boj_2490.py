#윷놀이
import sys

for _ in range(3):
    yout = sys.stdin.readline().rstrip().split()

    if yout.count('0') == 1 and yout.count('1') == 3:
        print('A')
    elif yout.count('0') == 2 and yout.count('1') == 2:
        print('B')
    elif yout.count('0') == 3 and yout.count('1') == 1:
        print('C')
    elif yout.count('0') == 4:
        print('D')
    elif yout.count('1') == 4:
        print('E')