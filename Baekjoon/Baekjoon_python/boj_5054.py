#주차의 신
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    locations = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

    print((locations[-1] - locations[0]) * 2)