#탄산 음료
import sys

e, f, c = map(int, sys.stdin.readline().rstrip().split())
e += f
bottle = 0

while True:
    bottle += (e // c)
    e = e // c + e % c

    if e < c:
        break
print(bottle)