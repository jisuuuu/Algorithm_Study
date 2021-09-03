#영석이와 친구들
import sys
n, m, l = map(int, sys.stdin.readline().rstrip().split())
friend = {i : 0 for i in range(1, n + 1)}

cnt = 0
idx = friend[1] = 1
while friend[idx] != m:
    if friend[idx] % 2 != 0:
        idx = n if (idx + l) % n == 0 else (idx + l) % n

    else:
        idx -= l
        if idx <= 0:
            idx += n

    friend[idx] += 1
    cnt += 1

print(cnt)