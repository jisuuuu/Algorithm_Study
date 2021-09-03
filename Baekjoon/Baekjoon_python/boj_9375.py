#패션왕 신해빈
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    wear = {}
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split()

        if type in wear:
            wear[type] += 1
        else:
            wear[type] = 1

    cnt = 1
    for key in wear:
        cnt *= (wear[key] + 1)
    print(cnt - 1)