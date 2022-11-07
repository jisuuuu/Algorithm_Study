#가장 큰 금민수
import sys
n = int(sys.stdin.readline().rstrip())

while True:
    if len(str(n)) == str(n).count('4') + str(n).count('7'):
        print(n)
        break
    n -= 1