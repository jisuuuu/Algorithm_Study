#주사위 게임
import sys
n = int(sys.stdin.readline().rstrip())
changyoung = sangduk = 100

for _ in range(n):
    c, s = map(int, sys.stdin.readline().rstrip().split())

    if c < s:
        changyoung -= s
    elif c > s:
        sangduk -= c

print(changyoung)
print(sangduk)