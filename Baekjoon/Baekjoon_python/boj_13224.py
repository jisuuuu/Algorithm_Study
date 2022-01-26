#Chop Cup
import sys
moves = sys.stdin.readline().rstrip()
cups = [1, 0, 0]

for m in moves:
    if m == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif m == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    elif m == 'C':
        cups[0], cups[2] = cups[2], cups[0]

print(cups.index(1) + 1)