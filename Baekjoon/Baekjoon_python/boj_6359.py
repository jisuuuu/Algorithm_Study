#만취한 상범
import sys


def solve(rooms, k, n):
    if k == n + 1:
        print(rooms.count(1))
        return

    for i in range(k - 1, n, k):
        if rooms[i] == 0:
            rooms[i] = 1
        elif rooms[i] == 1:
            rooms[i] = 0
    solve(rooms, k + 1, n)


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    rooms = [0 for _ in range(n)]
    solve(rooms, 1, n)