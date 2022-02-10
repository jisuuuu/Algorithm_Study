#대회 자리
import sys
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    p, m = map(int, sys.stdin.readline().rstrip().split())
    seats = [0 for i in range(m)]
    cnt = 0
    for _ in range(p):
        person = int(sys.stdin.readline().rstrip()) - 1
        if seats[person] == 0:
            seats[person] = 1
        else:
            cnt += 1
    print(cnt)