#꿍의 우주여행
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, d = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0

    for _ in range(n):
        v, f, c = map(int, sys.stdin.readline().rstrip().split())

        if v * (f / c) >= d:
            cnt += 1
    print(cnt)