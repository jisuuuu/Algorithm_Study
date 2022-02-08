#0의 개수
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = sys.stdin.readline().rstrip().split()
    cnt = 0

    for i in range(int(n), int(m) + 1):
        cnt += str(i).count('0')
    print(cnt)