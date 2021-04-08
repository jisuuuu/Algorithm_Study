#하노이 탑 이동 순서
import sys


def hanoi(n, f, z, t):
    if n == 0:
        return
    hanoi(n - 1, f, t, z)
    move.append((f, t))
    hanoi(n - 1, z, f, t)


move = []
n = int(sys.stdin.readline().rstrip())
hanoi(n, 1, 2, 3)

print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))