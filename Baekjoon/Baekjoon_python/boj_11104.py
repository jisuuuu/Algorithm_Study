#Fridge of Your Dreams
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    num = sys.stdin.readline().rstrip().lstrip('0')
    print(int('0b' + num, 2))