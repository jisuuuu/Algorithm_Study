#개표
import sys
n = int(sys.stdin.readline().rstrip())
v = sys.stdin.readline().rstrip()
a = b = 0

for w in v:
    if w == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')