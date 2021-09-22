#Winning Score
import sys
apple = 0
banana = 0

for i in range(3, 0, -1):
    apple += int(sys.stdin.readline().rstrip()) * i

for i in range(3, 0, -1):
    banana += int(sys.stdin.readline().rstrip()) * i

if apple < banana:
    print('B')
elif apple > banana:
    print('A')
else:
    print('T')
