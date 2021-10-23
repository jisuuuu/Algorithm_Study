#2007년
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

import sys
x, y = map(int, sys.stdin.readline().rstrip().split())

day = 0

for i in range(0, x - 1):
    day += months[i]

day = (day + y) % 7
print(days[day])