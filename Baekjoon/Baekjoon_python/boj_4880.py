#다음수
import sys

while True:
    a1, a2, a3 = map(int, sys.stdin.readline().rstrip().split())

    if a1 == 0 and a2 == 0 and a3 == 0:
        break

    if a2 - a1 == a3 - a2:
        print(f'AP {a3 + (a2 - a1)}')
    elif a2 // a1 == a3 // a2:
        print(f'GP {a3 * (a2 // a1)}')