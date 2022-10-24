#Quicksum
import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '#':
        break

    total = 0
    for i, w in enumerate(word):
        if w != ' ':
            total += ((ord(w) - 64) * (i + 1))
    print(total)